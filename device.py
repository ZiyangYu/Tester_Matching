import os
import csv

#parsing the csv file
with open('devices.csv') as csvfile:
	deviceReader = csv.reader(csvfile)
	devices = list(deviceReader)
	size = len(devices)

def getDeviceIDByDescrip(description):
	"""
	Get a Device ID by a device Description

	Args:
	description: description of the device

    Returns:
    the device ID
    """
	for device in devices:
		if(description == device[1]):
			return device[0]

def getDescripByDeviceID(ID):
	"""
	Get a Device description by a device ID

	Args:
	ID: the device ID

    Returns:
    the device description
    """
	for device in devices:
		if(ID == device[0]):
			return device[1]
