import os
import csv
import testers

with open('bugs.csv') as csvfile:
	bugsReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	bugs = list(bugsReader)
	bugs.pop(0)
	size = len(bugs)

def getBugsByCriteria(Countries, Devices):
	lBugs_Country = []
	lBugs_Country_Device = []
	#get a list of bug ID with required Countries
	if(Countries[0] == 'ALL'):
		lBugs_Country = bugs
	else :
		for bug in bugs: 
			bugTesterID = int(bug[2])
			for Country in Countries:
				if(Country == testers.getCountryByTesterID(bugTesterID)):
					lBugs_Country.append(bug)
	return lBugs_Country

c = ['US','JP']
e = ['JP']
f = ['US']
d = ['df']
g = ['ALL']

print(getBugsByCriteria(c,d))
print(size)
print(len(getBugsByCriteria(c,d)))
print(len(getBugsByCriteria(e,d)))
print(len(getBugsByCriteria(f,d)))
print(len(getBugsByCriteria(g,d)))



