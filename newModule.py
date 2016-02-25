import sys
import collections
import os

#currently have removed all symlinks and mapped files to directories

depDict = dict()
indDict = dict()

depPath = "/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/"
indPath = "/software/modules/modulefiles_static/"

#Using os.walk and [1] to isolate directories ONLY in this folder. Use [0] to get root and [2] for any files.
#returns a list
moduleDep = os.walk(depPath).next()[1]
#Java modules, run on all modules
moduleInd = os.walk(indPath).next()[1]

def fileParse (fileItem):
	versionFile = open("fileItem", "r")
	versionContent = versionFile.read()
	versionList = versionContent.split()
	itemType = dict()

	for index, part in enumerate(versionList):
		if 'set' in part:
			#item description is 2 away from set value
			itemDescription = versionList[index+2]
			#item is 1 away from set value
			itemType[versionList[index+1]] = itemDescription
		elif 'module-whatis' in part:
			moduleWhatIs = versionList[index+1]
		else: 
			continue

	return itemType

def mainParse (path):
	mainDict = dict()
	versionsDict = dict()

	for root, dirs, files in os.walk(path):
		if root is path:
			continue

		#iterating over a slice copy of the list, or will modify original list and screw it up
		for index, item in enumerate(files[:]):
			if os.path.islink(os.path.join(root,item)):
				files.remove(item)

			#ensures we only parse first item, since we don't need the rest
			if index is 1:
				versionsDict = fileParse(item)

			#will work on parsing files 


		#normpath removes any trailing slashes
		#basename gives me last part of path after last slash
		mainDict[os.path.basename(os.path.normpath(root))] = files 
		#append versionsDict

	orderedDict = collections.OrderedDict(sorted(mainDict.items()))

	return orderedDict

depDict = mainParse(depPath)
indDict = mainParse(indPath)

for key, value in depDict.iteritems():
	print key
	print value



