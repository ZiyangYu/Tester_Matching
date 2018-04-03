"""
Main file to run the program.
Created by Ziyang Yu
"""
import os
import bugs
import testers
import device

def getNumberOfBugsByTesterID(ID, Bugs):
	"""
	Get the amount of bugs that an tester filed

	Args:
	ID: The ID number of the tester
	Bugs: A list of bugs

    Returns:
    The amount of bugs that tester filed in the list of bugs
    """

    #bug counter
	count = 0
	#Iterate through the bug list, if there is one that the tester filed,
	#the counter will add up by one
	for Bug in Bugs:
		if(int(Bug[2]) == ID):
			count += 1
	return count

def runTest_Matcher(Countries, Devices):
	"""
	Main function of the program, calcute the result based
	the criteria provided

	Args:
	Countries: A List of Country that is a part of criteria
	Devices: A List of Device that is a part of criteria

    Returns:
    A dirctionary of results. Ranked with descending order.
    key is Tester ID, value is the experience
    """

    #get a list of bugs that matches the criteria
	matchedBugs = bugs.getBugsByCriteria(Countries, Devices)
	print('==================================================')
	print('Results: ')
	print(' ')
	print('Total number of bugs that match with given criteria: \n')

	#get a list of all the testers' id
	lTesterIDs = testers.getListOfTesterID()
	print(len(matchedBugs))

	#the original result, unsorted
	Results = {}
	for ID in lTesterIDs:
		tNum = getNumberOfBugsByTesterID(ID, matchedBugs)
		Results[ID] = tNum

	#the sorted result
	sorted_Result = {}
	sorted_List = sorted(Results.values(), reverse=True)

	for sortedKey in sorted_List:
		for key, value in Results.items():
			if value == sortedKey:
				sorted_Result[key] = value

	print(' ')	
	print('Result with Experiences : ')	

	#print out the result
	for key, value in sorted_Result.items():
		#get tester's name
		name = testers.getTesterNameByID(key)
		print(name[0] + ' '+ name[1] +' => '+ str(value))	

	print(' ')
	print('************************************************')	
	print(' ')
	return sorted_Result

#==============================================================
#The Beginning of the program
print(' ')
print('*****************Test Matcher*******************')
print(' ')
print('Welcome!')
Input_Country = input('Please input a list of Countries or ALL for Test Results, Split with comma with no space ",": \n')
Criteria_Countries = Input_Country.split(',')
print(' ')
Input_Device = input('Please input a list of devices for Test Results, Split with comma with no space ",": \n')
Criteria_Devices = Input_Device.split(',')
print(' ')

runTest_Matcher(Criteria_Countries, Criteria_Devices)
