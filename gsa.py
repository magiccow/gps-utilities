#!/usr/local/bin/python3
import serial
import re
import glob

def gsa(parts):
    results = {'mode':parts[1], 'mode2':parts[2], 'pdop':parts[15], 'hdop':parts[16], 'vdop':parts[17] }
    ids = []
    for i in range(3,15):
        id = parts[i]
        if id != '':
           ids.append( id )
    results['ids'] = ids
    return results 

def nmea(line):
    (sentence, checksum) = line.split('*')
    parts = sentence.split(",")
    if parts[0]=='$GPGSA':
        struct = gsa(parts)
        print(struct)

port = glob.glob('/dev/tty.usb*')[0]
ser = serial.Serial(port, timeout=2) 
line = ""
while True:
    line = ser.readline().decode('ascii', errors='ignore')
    nmea(line)

