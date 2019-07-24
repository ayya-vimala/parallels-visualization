#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
convert sutta parallel html data to json

"""
import os
import re
import json
import itertools

template = re.compile(r'^(dn\d+)')
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
					if re.match(r'^dn[0-9]$',cfoundvalue):
						cfoundvalue = 'dn0' + cfoundvalue[2]
					citem = item.split('#')[0].strip('~')
					if (citem != cfoundvalue and len(citem) < 15):
						citem = re.split(r'[0-9]',citem)[0]
						citem = citem.split('-')[0]
						jsonlist.append([cfoundvalue,citem])

sankeylist = []
dnlist = jsonlist

for item in jsonlist:
	counter = jsonlist.count(item)
	sankeylist.append([item[0],item[1],counter])

sankeylist = sorted(sankeylist)
dedup = [sankeylist[i] for i in range(len(sankeylist)) if i == 0 or sankeylist[i] != sankeylist[i-1]]

with open('dn.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)


template = re.compile(r'^(mn\d+)')
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
					if re.match(r'^mn[0-9]$',cfoundvalue):
						cfoundvalue = 'mn00' + cfoundvalue[2]
					elif re.match(r'^mn[0-9][0-9]$',cfoundvalue):
						cfoundvalue = 'mn0' + cfoundvalue[2] + cfoundvalue[3]
					citem = item.split('#')[0].strip('~')
					if (citem != cfoundvalue and len(citem) < 15):
						citem = re.split(r'[0-9]',citem)[0]
						citem = citem.split('-')[0]
						if (citem == 'g'):
							print(item)
						jsonlist.append([cfoundvalue,citem])

sankeylist = []
mnlist = jsonlist

for item in jsonlist:
	counter = jsonlist.count(item)
	sankeylist.append([item[0],item[1],counter])

sankeylist = sorted(sankeylist)
dedup = [sankeylist[i] for i in range(len(sankeylist)) if i == 0 or sankeylist[i] != sankeylist[i-1]]

with open('mn.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)



template = re.compile(r'^(an\d+)')
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
					if re.match(r'^an[0-9]$',cfoundvalue):
						cfoundvalue = 'an0' + cfoundvalue[2]
					citem = item.split('#')[0].strip('~')
					if (citem != cfoundvalue and len(citem) < 15):
						citem = re.split(r'[0-9]',citem)[0]
						citem = citem.split('-')[0]
						jsonlist.append([cfoundvalue,citem])

sankeylist = []
anlist = jsonlist

for item in jsonlist:
	counter = jsonlist.count(item)
	sankeylist.append([item[0],item[1],counter])

sankeylist = sorted(sankeylist)
dedup = [sankeylist[i] for i in range(len(sankeylist)) if i == 0 or sankeylist[i] != sankeylist[i-1]]

with open('an.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)



template = re.compile(r'^(sn\d+)')
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
					if re.match(r'^sn[0-9]$',cfoundvalue):
						cfoundvalue = 'sn0' + cfoundvalue[2]
					citem = item.split('#')[0].strip('~')
					if (citem != cfoundvalue and len(citem) < 15):
						citem = re.split(r'[0-9]',citem)[0]
						citem = citem.split('-')[0]
						jsonlist.append([cfoundvalue,citem])

sankeylist = []
snlist = jsonlist

for item in jsonlist:
	counter = jsonlist.count(item)
	sankeylist.append([item[0],item[1],counter])

sankeylist = sorted(sankeylist)
dedup = [sankeylist[i] for i in range(len(sankeylist)) if i == 0 or sankeylist[i] != sankeylist[i-1]]

with open('sn.json', 'w') as outfile:
	json.dump(dedup, outfile, indent=4)



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