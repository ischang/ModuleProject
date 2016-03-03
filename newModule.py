import sys
import collections
import os
import json
import re

#currently have removed all symlinks and mapped files to directories

depDict = dict()
indDict = dict()

depPath = "/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/"
indPath = "/software/modules/modulefiles_static/"
#depPath = "/home/phreell/Desktop/moduleind/modulefiles"
#Using os.walk and [1] to isolate directories ONLY in this folder. Use [0] to get root and [2] for any files.
#returns a list
moduleDep = os.walk(depPath).next()[1]
#Java modules, run on all modules
moduleInd = os.walk(indPath).next()[1]

def fileParse (root, filePath):
	versionFile = open(os.path.join(root,filePath), "r")
	versionContent = versionFile.read()
	newDict = dict()

	#Regex the variables into results
	pattern = re.compile("set\s(\w+)\s\"(.+?)?\"", re.DOTALL)
	results = re.findall(pattern, versionContent)

	if 'static' in root:
		osType = 'independent'

	elif 'x86_64-linux-ubuntu14.04' in root:
		osType = 'x86_64-linux-ubuntu14.04'

	else:
		osType = ''

	for item in results:
		#why doesn't R let me insert OS?? suspecT! 
		tempItem = []
		tempItem.append(osType)
		newDict['os'] = tempItem

		#don't want swroot, so continue
		if 'swroot' in item[0]:
			continue
		#\n appears when there's no description
		#only when in code -- is there a better way to parse this out?
		elif '\n' in item[1]:
			continue
		#change note to description per adam's format
		elif item[0] == 'note':
			newDict['description'] = item[1]
			continue 

		elif item[0] == 'os':
			if not osType:
				continue 

		if item[0] == 'tags':
			newDict['tags'] = item[1].split(',')
			continue
		else:
			newDict['tags'] = []

		newDict[item[0]]= item[1]

	return newDict
#all cluster cabernet so far??? only one we care about until 16 comes out
	
def mainParse (path):
	mainDict = dict()
	versionsDict = dict()
	fileDict = dict()
	listAll = []

	for root, dirs, files in os.walk(path):
		if root is path:
			continue

		#iterating over a slice copy of the list, or will modify original list and screw it up
		for index, item in enumerate(files[:]):
			if os.path.islink(os.path.join(root,item)):
				files.remove(item)

			#ensures we only parse first item, since we don't need the rest
			if index is 0:
				filesDict = fileParse(root, item)

			#will work on parsing files 


		#normpath removes any trailing slashes
		#basename gives me last part of path after last slash
		#replaces version with the full amount of versions
		filesDict["versions"] = files
		filesDict["name"] = os.path.basename(os.path.normpath(root))
		#pop version and dir, since we want to replace it with 
		filesDict.pop("dir", None)
		filesDict.pop("version", None)
		mainDict[os.path.basename(os.path.normpath(root))] = filesDict
		#append versionsDict

	orderedDict = collections.OrderedDict(sorted(mainDict.items()))

	return orderedDict

def jsonDump (jsonDict, pathJson): 
	with open(pathJson,'w') as fp:
		json.dump([], fp)
	with open(pathJson,'r') as fp2:
		fp3 = json.load(fp2)
	tempDict = dict()
	for key, value in jsonDict.iteritems():
		tempDict = jsonDict[key]
		with open(pathJson, mode = 'w') as fp2:
			fp3.append(tempDict)
			json.dump(fp3, fp2)

depDict = mainParse(depPath)
indDict = mainParse(indPath)

jsonDump(depDict, "depResults.json")
jsonDump(indDict, "indResults.json")

with open("depResults.json", 'r') as dep:
	dep2 = json.load(dep)

with open ("indResults.json", "r") as ind:
	ind2 = json.load(ind)

with open ("results.json", "w") as fp:
	json.dump([], fp)

with open("results.json", "w") as fp2:
	dep2.append(ind2)
	json.dump(dep2, fp2)

#The ugliest code in all of humanity is below (and it's still not the right format!): 
#for key, value in depDict.iteritems():
#	tempDict = dict()
#	sys.stdout.write('{')
#	tempDict = depDict[key]
#	for key2 in tempDict:
#		sys.stdout.write(key2)
#		sys.stdout.write(":")
#		if tempDict[key2] is list:
#			sys.stdout.write(tempDict[key2])
#		else:
#			blah = str(tempDict[key2])
#			sys.stdout.write ("\'")
#			sys.stdout.write(blah)
#			sys.stdout.write("\'")
#		sys.stdout.write(',')
#	sys.stdout.write ("}")
#	print (",")


#for key, value in depDict.iteritems():
#	print key
#	print valu#e#

#count = 0 
#for key, value in depDict.iteritems():
#	if os.path.isfile('result.json'):
#		with open('result.json') as fp:
#			data = json.load(fp)#

#		data.update(depDict[key])
#		with open('result.json') as fp:
#			json.dump(data,fp)
#	else:
#		with open('result.json', 'w') as fp:
#			json.dump(depDict[key], fp)#

	#RETURN DICTIONARY
	#do line by line instead
	#versionList = versionContent.split()asfsd
	#itemType = dict()
#
	#for index, part in enumerate(versionList):
	#	if 'set' in part:
	#		#item description is 2 away from set value
	#		itemDescription = versionList[index+2]
	#		#item is 1 away from set value
	#		itemType[versionList[index+1]] = itemDescription
	#	elif 'module-whatis' in part:
	#		moduleWhatIs = versionList[index+1]
	#	else: 
	#		continue
#
	#return itemType
