import sys
import collections
import os

#currently have removed all symlinks and mapped files to directories

depDict = dict()
indDict = dict()
meow = []

depPath = "/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/"
indPath = "/software/modules/modulefiles_static/"

#Using os.walk and [1] to isolate directories ONLY in this folder. Use [0] to get root and [2] for any files.
#returns a list
moduleDep = os.walk(depPath).next()[1]
#Java modules, run on all modules
moduleInd = os.walk(indPath).next()[1]

#dependent
for root, dirs, files in os.walk(depPath):
	if root is depPath:
		continue

	#iterating over a slice copy of the list, or will modify original list and screw it up
	for item in files[:]:
		if os.path.islink(os.path.join(root,item)):
			files.remove(item)

	#normpath removes trailing slashes
	#basename gives me last part of path after last slash
	depDict[os.path.basename(os.path.normpath(root))] = files


orderedDict = collections.OrderedDict(sorted(depDict.items()))
for key, value in orderedDict.iteritems():
	print key
	print value

#print "ind: " 
#for file in moduleInd:
#	depDict[file]
#	print file

#ignore link

#def mainParse (path, dictionary)
