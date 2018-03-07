import os
import csv
import testers
import device

with open('bugs.csv') as csvfile:
	bugsReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	bugs = list(bugsReader)
	bugs.pop(0)
	size = len(bugs)

def getBugsByCriteria(Countries, Devices):
	lBugs_Country = []
	lBugs_Country_Device = []

	#get a list of bug with required Countries
	if(Countries[0] == 'ALL'):
		lBugs_Country = bugs
	else :
		for bug in bugs: 
			bugTesterCountry = testers.getCountryByTesterID(int(bug[2]))
			for Country in Countries:
				if(Country == bugTesterCountry):
					lBugs_Country.append(bug)

	#get a list of bug that matches both country and device criteria
	for bug in lBugs_Country:
		bugDevice = device.getDescripByDeviceID(bug[1])
		for Device in Devices:
			if(Device == bugDevice):
				lBugs_Country_Device.append(bug)

	return lBugs_Country_Device

#c = ['US','JP']
#e = ['JP']
#f = ['US']
#d = ['iPhone 4','iPhone 5']
#h = ['iPhone 5']
#g = ['ALL']

#print(getBugsByCriteria(c,d))
#print(size)
#print(len(getBugsByCriteria(c,d)))
#print(len(getBugsByCriteria(e,d)))
#print(len(getBugsByCriteria(f,d)))
#print(len(getBugsByCriteria(g,h)))



