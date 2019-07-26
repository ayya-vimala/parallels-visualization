#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
convert sutta parallel html data to json

"""
import os
import re
import json
import itertools

collections_dic = {
              "dn": "Digha Nikaya",
              "da": "Dīrghāgama",
              "mn": "Majjhima Nikaya",
              "ma": "Madhyamāgama",
              "sn": "Samyutta Nikaya",
              "sa": "Saṃyuktāgama",
              "an": "Anguttara Nikaya",
              "ea": "Ekottarikāgama",
              "kp": "Khuddakapāṭha",
				"dhp": "Dhammapada",
				"ud": "Udāna",
				"iti": "Itivuttaka",
				"snp": "Suttanipāta",
				"vv": "Vimānavatthu",
				"pv": "Petavatthu",
				"thag": "Theragāthā",
				"thig": "Therīgāthā",
				"tha": "Therāpadāna",
				"thi": "Therīapadāna",
				"bv": "Buddhavaṃsa",
				"cp": "Cariyāpiṭaka",
				"ja": "Jātaka",
				"mnd": "Mahāniddesa",
				"cnd": "Cūḷaniddesa",
				"ps": "Paṭisambhidāmagga",
				"ne": "Netti",
				"pe": "Peṭakopadesa",
				"mil": "Milindapañha",
				"t": "Other Chinese Suttas",
				"d": "Tibetan Suttas",
				"pli": "Pali Vinaya",
				"lzh": "Chinese Vinaya",
				"san": "Sanskrit Vinaya"
				}

collectionsList = ["dn", "da", "mn", "ma", "sn", "sa", "an", "ea", "kp","dhp","ud","iti","snp","vv","pv","thag","thig","tha","thi","bv","cp","ja","mnd","cnd","ps","ne","pe","mil","t","d","pli","lzh","san"]

kncollections_dic = {
			"kp": "Khuddakapāṭha",
			"dhp": "Dhammapada",
			"ud": "Udāna",
			"iti": "Itivuttaka",
			"snp": "Suttanipāta",
			"vv": "Vimānavatthu",
			"pv": "Petavatthu",
			"thag": "Theragāthā",
			"thig": "Therīgāthā",
			"tha": "Therāpadāna",
			"thi": "Therīapadāna",
			"bv": "Buddhavaṃsa",
			"cp": "Cariyāpiṭaka",
			"ja": "Jātaka",
			"mnd": "Mahāniddesa",
			"cnd": "Cūḷaniddesa",
			"ps": "Paṭisambhidāmagga",
			"ne": "Netti",
			"pe": "Peṭakopadesa",
			"mil": "Milindapañha",
			}

othercollections = { "arv": "Arthaviniścaya",
              "avs": "Avadānaśataka",
              "divy": "Divyāvadāna",
              "ds": "Dhammasaṅgaṇī",
              "g": "Gāndhārī Dharmapada 3",
              "gdhp": "Gāndhārī Dharmapada",
              "gf": "Gāndhārī fragments",
              "kf": "Khotanese fragments",
              "kv": "Kathāvatthu",
              "lal": "Lalitavistara",
              "pdhp": "Patna Dharmapada",
              "pf": "Prākrit fragments",
              "pp": "Puggalapaññatti",
              "sag": "Śarīrārthagāthā",
              "sf": "Sanskrit Fragments",
              "sht": "SHT fragments",
              "ud": "Udāna",
              "uf": "Uighur fragments",
              "up": "Upāyikā",
              "uv": "Udānavarga",
              "uvs": "Udānavarga de Subaši",
              "vb": "Vibhaṅga",
              }



def buildJson(collection,nrs0):
	template = re.compile(r'^('+collection+r'\d+)')
	jsonlist = []

	with open('parallels.json') as parallels_file:
		data = json.load(parallels_file)
		for p in data:

			try:
				plist = p['parallels']
			except:
				try:
					plist = p['mentions']
				except:
					plist = p['retells']
			foundvalue = [item for item in plist if template.match(item)]

			if foundvalue:
				for item in plist:
					if item != foundvalue:
						cfoundvalue = foundvalue[0].split('#')[0].strip('~')
						cfoundvalue = cfoundvalue.split('.')[0]
						if nrs0 == 1:
							if re.match(r'^'+collection+r'[0-9]$',cfoundvalue):
								cfoundvalue = collection+'0' + cfoundvalue[2]
						if nrs0 == 2:
							if re.match(r'^'+collection+r'[0-9]$',cfoundvalue):
								cfoundvalue = collection+'00' + cfoundvalue[2]
							elif re.match(r'^'+collection+r'[0-9][0-9]$',cfoundvalue):
								cfoundvalue = collection+'0' + cfoundvalue[2] + cfoundvalue[3]

						citem = item.split('#')[0].strip('~')
						if (citem != cfoundvalue and len(citem) < 15):
							citem = re.split(r'[0-9]',citem)[0]
							citem = citem.split('-')[0]
							jsonlist.append([cfoundvalue,citem])

	sankeylist = []

	jsonlist = sortList(jsonlist)
	for item in jsonlist:
		counter = jsonlist.count(item)
		sankeylist.append([item[0],item[1],counter])

	sankeylist = sorted(sankeylist)
	dedup = [sankeylist[i] for i in range(len(sankeylist)) if i == 0 or sankeylist[i] != sankeylist[i-1]]

	with open(collection+'.json', 'w') as outfile:
		json.dump(dedup, outfile, indent=4)

	return jsonlist


def sortList(inputlist):
	outputlist = [];
	for item in inputlist:
		newItem1 = '99_other'
		if item[1] in collectionsList:
			newItem1 = format(collectionsList.index(item[1]), '02d') +' '+ item[1]
		outputlist.append([item[0],newItem1])
	return sorted(outputlist)


dnlist = buildJson('dn',1);
anlist = buildJson('an',1);
snlist = buildJson('sn',1);
mnlist = buildJson('mn',2);

totalslist = []

for item in dnlist:
	totalslist.append(['1 dn',item[1]])
for item in mnlist:
	totalslist.append(['2 mn',item[1]])
for item in snlist:
	totalslist.append(['3 sn',item[1]])
for item in anlist:
	totalslist.append(['4 an',item[1]])

totalscounted = []

for item in totalslist:
	counter = totalslist.count(item)
	totalscounted.append([item[0],item[1],counter])

totalscounted = sorted(totalscounted)
dedup = [totalscounted[i] for i in range(len(totalscounted)) if i == 0 or totalscounted[i] != totalscounted[i-1]]

with open('suttas.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)
