import sys

moduleFile = open('module.txt', 'r') 
content = moduleFile.read()
partList = content.split()
partList = '\n'.join(partList)
#htmlFile = open('pretty.html', 'w'

print partList
	
#print the paths of the lines when it's /software

#print "hello from the other side"

moduleFile.close() 
