import sys
from jinja2 import Template, Environment, FileSystemLoader
import collections
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

moduleFile = open('module.txt', 'r') 
content = moduleFile.read()
programDict = dict()
partList = content.split()
#htmlFile = open('pretty.html', 'w'

for part in partList: 
	if '/' in part:
		if 'software' in part:
			continue
		else:	
			versionPart = part.split('/')
			if versionPart[0] in programDict:
				programDict[versionPart[0]].append(versionPart[1])

			elif versionPart[0] not in programDict:
				programDict[versionPart[0]] = [versionPart[1]]

	elif '/' not in part:
		if '3.2.10' in part:
			continue
		if '--' in part:
			continue
		if '-' in part and len(part) is 1:
			continue 

		programDict[part] = [""]

orderedDict = collections.OrderedDict(sorted(programDict.items()))
for key, value in orderedDict.iteritems():
	print key
	print value

#helloFile = open('index.html', 'r') 
theTemplate = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True, extensions = ['jinja2.ext.loopcontrols'])
#template = Template(helloFile.read())
#print template.render(software = orderedDict)
helloFile = open('index.html', 'w')

helloFile.write(theTemplate.get_template('template.html').render(software = orderedDict))
#print the paths of the lines when it's /software

#print "hello from the other side"
helloFile.close()
moduleFile.close() 
