import os
import csv
import testers
import device

#parsing the csv file
with open('bugs.csv') as csvfile:
	bugsReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	bugs = list(bugsReader)
	bugs.pop(0)
	size = len(bugs)

def getBugsByCriteria(Countries, Devices):
	"""
	Get a List of bugs that matches the criteria

	Args:
	Countries: A List of Country that is a part of criteria
	Devices: A List of Device that is a part of criteria

    Returns:
    A list of bugs that matches the criteria
    """
    #Empty lists for outputs
	lBugs_Country = []
	lBugs_Country_Device = []

	#get a list of bug with required Countries
	#Check if ALL countries are required
	if(Countries[0] == 'ALL'):
		lBugs_Country = bugs
	#If not, will go through every bug and append the one that matches
	#the criteria to an empty list
	else :
		for bug in bugs: 
			bugTesterCountry = testers.getCountryByTesterID(int(bug[2]))
			for Country in Countries:
				if(Country == bugTesterCountry):
					lBugs_Country.append(bug)

	#get a list of bug that matches both country and device criteria
	#Iterate through every bug that matches the country criteria,
	#append the one that matches the device criteria to an empty list
	for bug in lBugs_Country:
		bugDevice = device.getDescripByDeviceID(bug[1])
		for Device in Devices:
			if(Device == bugDevice):
				lBugs_Country_Device.append(bug)

	return lBugs_Country_Device
