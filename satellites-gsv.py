#!/usr/local/bin/python3
import serial
import json
import glob
import re

# identity of satellites - see https://en.wikipedia.org/wiki/List_of_GPS_satellites
birds = [
"dummy",    1660,
"USA-232",	2011,
"USA-180",	2004,
"USA-258",	2014,
"USA-289",  2018,
"USA-206",	2009,
"USA-251",	2014,
"USA-201",	2008,
"USA-262",	2015,
"USA-256",	2014,
"USA-265",	2015,
"USA-145",	1999,
"USA-192",	2006,
"USA-132",	1997,
"USA-154",	2000,
"USA-196",	2007,
"USA-166",  2003,
"USA-183",	2005,
"USA-96",   1993,
"USA-177",	2004,
"USA-150",	2000,
"USA-168",	2003,
"USA-175",	2003,
"USA-178",	2004,
"USA-239",	2012,
"USA-213",	2010,
"USA-260",	2015,
"USA-242",	2013,
"USA-151",	2000,
"USA-199",	2007,
"USA-248",	2014,
"USA-190",	2006,
"USA-266",	2016
]

def lookup_sat_info(index):
	satname = birds[2*index]
	year = birds[2*index+1]
	return satname, year


def extract_fields_gsv(raw_line):
    fields = {}
    m = re.match('(.+)\*\d+', raw_line)
    if m:
        line = m.group(1)
        items = line.split(',')
        fields['total_segments'] = items[1]
        fields['segment'] = items[2]
        fields['satellite_count'] = items[3]
        offset = 4
        sat_unit = []
        try:
            while not '*' in items[offset]:
                unit = {'PRN':items[offset],
                        'elevation':items[offset+1],
                        'azimuth':items[offset+2],
                        'SNR':items[offset+3]}
                satname, year = lookup_sat_info(int(unit['PRN']))
                unit['satname'] = satname
                unit['launch_date'] = year
                sat_unit.append(unit)
                offset += 4
        except IndexError:
            pass
        fields['sat_unit'] = sat_unit
    return fields

# open the COM port and start processing
comport = glob.glob('/dev/tty.usb*')[0]
with serial.Serial(comport, 9600, timeout=1) as ser:
	while True:
			line = ser.readline().decode('ascii',errors='ignore').rstrip('\r\n')
			if '$GPGSV' in line:
					fields = extract_fields_gsv(line)
					print(json.dumps(fields, indent=4))
					#print(json.dumps(fields))

