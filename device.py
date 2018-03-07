import os
import csv

with open('devices.csv') as csvfile:
	deviceReader = csv.reader(csvfile)
	devices = list(deviceReader)
	size = len(devices)

def getDeviceIDByDescrip(description):
	for device in devices:
		if(description == device[1]):
			return device[0]
	return 'ERROR: NO DEVICE FOUND'

def getDescripByDeviceID(ID):
	for device in devices:
		if(ID == device[0]):
			return device[1]
	return 'ERROR: NO DEVICE FOUND'