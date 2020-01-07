#!/usr/local/bin/python3
import serial
import glob

comport = glob.glob('/dev/tty.usb*')[0]
print('Com port selected is: {}'.format(comport))
with serial.Serial(comport, 9600, timeout=1) as ser:
	while True:
			line = ser.readline().decode('ascii',errors='ignore').rstrip('\r\n')
			if '$GP' in line:
					print(line)

