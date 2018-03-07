import os
import csv

with open('testers.csv') as csvfile:
	testerReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	testers = list(testerReader)
	testers.pop(0)
	size = len(testers)

def getListOfTesterID():
	testerID = []
	for tester in testers:
		testerID.append(int(tester[0]))
	return testerID


def getTesterByID(ID):
	for tester in testers:
		if(ID == int(tester[0])):
			return tester
	return 'ERROR: NO TESTER FOUND'

def getTesterNameByID(ID):
	name = ['First Name', 'Last Name']
	for tester in testers:
		if(ID == int(tester[0])):
			name[0] = tester[1]
			name[1] = tester[2]
			return name
	return 'ERROR: NO TESTER NAME FOUND'

def getCountryByTesterID(ID):
	for tester in  testers:
		if(ID == int(tester[0])):
			return tester[3]

#print(getListOfTesterID())
#print(getTesterByID(8))
#print(getTesterNameByID(8))
#print(getCountryByTesterID(8))