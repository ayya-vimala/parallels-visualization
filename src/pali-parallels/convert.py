#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
convert sutta parallel html data to json

"""
import os
import re
import json
import itertools


collectionsList = ["dn", "da", "mn", "ma", "sn", "sa", "an", "ea", "kp","dhp","ud","iti","snp","vv","pv","thag","thig","tha","thi","bv","cp","ja","mnd","cnd","ps","ne","pe","mil","t","pli","lzh","san"]

kncollections = ["kp", "dhp", "ud", "iti", "snp", "vv", "pv", "thag", "thig", "tha-ap", "thi-ap", "bv", "cp", "ja", "mnd", "cnd", "ps", "ne", "pe", "mil"]

abcollections = ["ds", "vb", "dt", "pp", "kv", "ya", "patthana"]

sancollections = ["sf", "sht", "arv", "avs", "divy", "lal", "mkv", "sag", "sbh", 'uv', 'uvs']

tibcollections = ["d","up", "uv-kg"]

othercollections = { 
              "g": "Gāndhārī Dharmapada 3",
              "gdhp": "Gāndhārī Dharmapada",
              "gf": "Gāndhārī fragments",
              "kf": "Khotanese fragments",
              "pdhp": "Patna Dharmapada",
              "pf": "Prākrit fragments",
              "uf": "Uighur fragments",
              }

def buildKnJson():
	sankeylist = []
	for collection in kncollections:
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
							actualfoundvalue = foundvalue[0].split('#')[0]
							cfoundvalue = actualfoundvalue.split('.')[0]
							
							cfoundvalue = re.split(r'[0-9]',cfoundvalue)[0]

							citem = item.split('#')[0].strip('~')
							if (citem != actualfoundvalue and len(citem) < 15):
								citem = re.split(r'[0-9]',citem)[0]
								if (not citem.startswith("uv")):
									citem = citem.split('-')[0]
								jsonlist.append([cfoundvalue,citem])

		jsonlist = sortList(jsonlist)
		for item in jsonlist:
			counter = jsonlist.count(item)
			sankeylist.append([item[0],item[1],counter])

	sankeylist = addBlankEntries(sankeylist,'kn')

	newsankeylist = []
	for item in sankeylist:
		newsankeylist.append([format(kncollections.index(item[0]), '02d') +' '+item[0],item[1],item[2]])
	newsankeylist = sorted(newsankeylist)		
	dedup = [newsankeylist[i] for i in range(len(sankeylist)) if i == 0 or newsankeylist[i] != newsankeylist[i-1]]

	with open('kn.json', 'w') as outfile:
		json.dump(dedup, outfile, indent=4)

	return newsankeylist


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
						actualfoundvalue = foundvalue[0].split('#')[0]
						cfoundvalue = actualfoundvalue.split('.')[0]
						
						if nrs0 == 1:
							if re.match(r'^'+collection+r'[0-9]$',cfoundvalue):
								cfoundvalue = collection+'0' + cfoundvalue[2]
						if nrs0 == 2:
							if re.match(r'^'+collection+r'[0-9]$',cfoundvalue):
								cfoundvalue = collection+'00' + cfoundvalue[2]
							elif re.match(r'^'+collection+r'[0-9][0-9]$',cfoundvalue):
								cfoundvalue = collection+'0' + cfoundvalue[2] + cfoundvalue[3]

						citem = item.split('#')[0].strip('~')
						if (citem != actualfoundvalue and len(citem) < 15):
							citem = re.split(r'[0-9]',citem)[0]
							if (not citem.startswith("uv")):
								citem = citem.split('-')[0]
							jsonlist.append([cfoundvalue,citem])

	sankeylist = []

	jsonlist = sortList(jsonlist)
	for item in jsonlist:
		counter = jsonlist.count(item)
		sankeylist.append([item[0],item[1],counter])

	sankeylist = addBlankEntries(sankeylist,collection)
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
		if item[1] in sancollections:
			newItem1 = "40_sanskrit"
		if item[1] in tibcollections:
			newItem1 = "60_tibetan"
		if item[1] in abcollections:
			newItem1 = "70_abhidhamma"
		outputlist.append([item[0],newItem1])
	return sorted(outputlist)

def addBlankEntries(inputlist,collection):
	colnr = collection+'01'
	if collection == 'kn':
		colnr = 'kp'
	if collection == 'mn':
		colnr = 'mn001'
	if collection == 'sutta':
		colnr = '1 dn'
	targetnrlist = []
	for item in inputlist:
		if item[0] == colnr:
			targetnrlist.append(item[1][3:])
	for item in collectionsList:
		if item not in targetnrlist:
			inputlist.append([colnr,format(collectionsList.index(item), '02d') +' '+ item,0])
	return inputlist


dnlist = buildJson('dn',1)
anlist = buildJson('an',1)
snlist = buildJson('sn',1)
mnlist = buildJson('mn',2)
knlist = buildKnJson()

totalslist = []

for item in dnlist:
	totalslist.append(['1 dn',item[1]])
for item in mnlist:
	totalslist.append(['2 mn',item[1]])
for item in snlist:
	totalslist.append(['3 sn',item[1]])
for item in anlist:
	totalslist.append(['4 an',item[1]])
for item in knlist:
	totalslist.append(['5 kn',item[1]])

totalscounted = []

for item in totalslist:
	counter = totalslist.count(item)
	totalscounted.append([item[0],item[1],counter])

totalscounted = addBlankEntries(totalscounted,'sutta')
totalscounted = sorted(totalscounted)
dedup = [totalscounted[i] for i in range(len(totalscounted)) if i == 0 or totalscounted[i] != totalscounted[i-1]]

with open('suttas.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)
