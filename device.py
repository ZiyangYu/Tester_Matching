import os
import csv

with open('devices.csv') as csvfile:
	deviceReader = csv.reader(csvfile)
	devices = list(deviceReader)
	size = len(devices)

def getDeviceIDByDescrip(description):
	i = 0
	for device in devices:
		if(description == devices[i][1]):
			return devices[i][0]
		else:
			i+=1
	return 'ERROR: NO DEVICE FOUND'

print(getDeviceIDByDescrip('iPhone 5'))