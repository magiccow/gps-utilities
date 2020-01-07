#!/usr/local/bin/python3
import serial
import glob


def lookup(gp):
	nmea = {
      '$GPVTG' : 'Track made good and ground speed',
      '$GPRMC' : 'Recommended minimum specific GPS/TRANSIT data',
      '$GPGGA' : 'GPS fixed data', 
      '$GPGSA' : 'GPS dillution of precision and active satellites',
      '$GPGLL' : 'Geographical position, latitude and longitude',
      '$GPGSV' : 'GPS satellite in view'
    }
	return nmea.get(gp,'Unknown')
	



messageTypes = set() 
count = 0
max = 100

comport = glob.glob('/dev/tty.usb*')[0]
with serial.Serial(comport, 9600, timeout=1) as ser:
	print("Please wait a few seconds while I listen to port {}".format(comport))
	while count<max: 
		line = ser.readline().decode('ascii', errors='ignore')
		if '$GP' in line:
			items = line.split(',')
			messageTypes.add( items[0] ) 
			count += 1
		#print("Message Types seen = {}".format(messageTypes))

	for gp in messageTypes:
		print( "Message {} is '{}'".format( gp, lookup(gp) ) )
