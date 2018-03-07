import os
import csv

with open('tester_device.csv') as csvfile:
	tester_deviceReader = csv.reader(csvfile)
	#pop the first row of table entries, remaining pure data
	tester_devices = list(tester_deviceReader)
	tester_devices.pop(0)
	size = len(tester_devices)

print(tester_devices)