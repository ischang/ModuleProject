import sys
import collections
import os

os
moduleDep = os.listdir("/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/")
moduleInd = os.listdir("/software/modules/modulefiles_static/")

depDict = dict()
indDict = dict()

print "dep:" 
for root, dirs, files in os.walk("/software/modules/3.2.10/x86_64-linux-ubuntu14.04/Modules/3.2.10/modulefiles/"):
	print "root:"
	print root
	print "dirs:"
	print dirs
	print "files:"
	print files

#print "ind: " 
#for file in moduleInd:
#	depDict[file]
#	print file

#ignore link