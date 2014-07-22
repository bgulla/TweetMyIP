#!/usr/bin/python

FILE_PREPEND="data/"

def getStringFromFile(filename):
	val = ""
	with open(filename) as f:
		val = f.read()
	
	return val.replace("\n","")

def writeStringToFile(filename,value):
	with open(filename,'w') as f:
		f.write(value)

def doesFileEqualString(filename, value):
	filestring = getStringFromFile(filename)
	if filestring == value:
		return True
	else:
		return False

#print doesFileEqualString("tmp.txt","turducken")
#print doesFileEqualString("tmp.txt","turducken2")



#print getStringFromFile("tmp.txt")

#writeStringToFile("tmp.txt","turducken")
