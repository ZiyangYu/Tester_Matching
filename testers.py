import os
import csv

#parsing the csv file
with open('testers.csv') as csvfile:
	testerReader = csv.reader(csvfile)

	#pop the first row of table entries, remaining pure data
	testers = list(testerReader)
	testers.pop(0)
	size = len(testers)

def getListOfTesterID():
	"""
	Get a list of tester's ID

    Returns:
    A list of every tester's ID
    """
    # Empty list that will hold testers' ID
	testerID = []

	#Iterate through every tester and append tester's ID to the list
	for tester in testers:
		testerID.append(int(tester[0]))
	return testerID

def getTesterByID(ID):
	"""
	Get a information of a tester by tester ID

	Args:
	ID: The ID number of the tester

    Returns:
    A list of tester's inforamtion with provided tester ID
    """
    #Iterate through all testers to find the matching ID then return
	for tester in testers:
		if(ID == int(tester[0])):
			return tester

def getTesterNameByID(ID):
	"""
	Get a tester's name by tester ID

	Args:
	ID: The ID number of the tester

    Returns:
    A list object of tester's name. [First Name, Last Name]
    """

    #Create a name List, then append tester's name to the list
	name = ['First Name', 'Last Name']
	for tester in testers:
		if(ID == int(tester[0])):
			name[0] = tester[1]
			name[1] = tester[2]
			return name

def getCountryByTesterID(ID):
	"""
	Get a tester's country by tester ID

	Args:
	ID: The ID number of the tester

    Returns:
    A String. The country of the tester
    """
    #Find the tester, then return the country
	for tester in  testers:
		if(ID == int(tester[0])):
			return tester[3]
