import os
import bugs
import testers
import device

def runTest_Matcher(Countries, Devices):
	matchedBugs = bugs.getBugsByCriteria(Countries, Devices)
	print(testers.getTesterByID(8))

print(' ')
print('*****************Test Matcher*******************')
print(' ')
print('Welcome!')
Input_Country = input('Please input a list of Countries for Test Results, Split with comma with no space ",": \n')
Criteria_Countries = Input_Country.split(',')
print(' ')
Input_Device = input('Please input a list of devices for Test Results, Split with comma with no space ",": \n')
Criteria_Devices = Input_Device.split(',')
print(' ')

runTest_Matcher(Criteria_Countries, Criteria_Devices)
