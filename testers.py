import os
import csv

with open('testers.csv') as csvfile:
	testerReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	testers = list(testerReader)
	testers.pop(0)
	size = len(testers)


def getTesterbyID(ID):
	i = 0
	for tester in testers:
		if(ID == int(testers[i][0])):
			return testers[i]
		else:
			i += 1
	return 'ERROR: NO TESTER FOUND'

def getTesterNamebyID(ID):
	name = ['First Name', 'Last Name']
	i = 0
	for tester in testers:
		if(ID == int(testers[i][0])):
			name[0] = testers[i][1]
			name[1] = testers[i][2]
			return name
		else:
			i += 1
	return 'ERROR: NO TESTER NAME FOUND'


print(getTesterbyID(8))
print(getTesterNamebyID(8))