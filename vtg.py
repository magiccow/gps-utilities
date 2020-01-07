#!/usr/local/bin/python3
import serial
import re
import glob

def vtg(parts):
    results = {}
    index = 1
    for part in ('course','reference','speed','units','speed-b','speed-b-units','mode'):
        results[part] = parts[index]
        index += 1
    return results 

def nmea(line):
    (sentence, checksum) = line.split('*')
    parts = sentence.split(",")
    if parts[0]=='$GPVTG':
        struct = vtg(parts)
        print(struct)

port = glob.glob('/dev/tty.usb*')[0]
ser = serial.Serial(port, timeout=2) 
line = ""
while True:
    line = ser.readline().decode('ascii', errors='ignore')
    nmea(line)

