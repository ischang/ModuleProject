import sys
import collections
import os

depDict = dict()
indDict = dict()

depPath = "/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/"
indPath = "/software/modules/modulefiles_static/"

#Using os.walk and [1] to isolate directories ONLY in this folder. Use [0] to get root and [2] for any files.
#returns a list
moduleDep = os.walk(depPath).next()[1]
#Java modules, run on all modules
moduleInd = os.walk(indPath).next()[1]

#dependent
for root, dirs, files in os.walk(depPath):
	print "root" 
	print root
	print "dirs"
	print dirs
	print "files"
	print files

#print "ind: " 
#for file in moduleInd:
#	depDict[file]
#	print file

#ignore link