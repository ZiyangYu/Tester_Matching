import os
import bugs
import testers
import device

def getNumberOfBugsByTesterID(ID, Bugs):
	count = 0
	for Bug in Bugs:
		if(int(Bug[2]) == ID):
			count += 1
	return count

def runTest_Matcher(Countries, Devices):
	matchedBugs = bugs.getBugsByCriteria(Countries, Devices)
	print('==================================================')
	print('Results: ')
	print(' ')
	print('Total number of bugs that match with given criteria: \n')
	lTesterIDs = testers.getListOfTesterID()
	print(len(matchedBugs))
	Results = {}
	for ID in lTesterIDs:
		Results[ID] = getNumberOfBugsByTesterID(ID, matchedBugs)
	sorted_Result = {}
	sorted_List = sorted(Results.values(), reverse=True)

	for sortedKey in sorted_List:
		for key, value in Results.items():
			if value == sortedKey:
				sorted_Result[key] = value

	print(' ')	
	print('Result with Experiences : ')	

	for key, value in sorted_Result.items():
		name = testers.getTesterNameByID(key)
		print(name[0] + ' '+ name[1] +' => '+ str(value))	

	print('************************************************')	


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
