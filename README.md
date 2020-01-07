# gps-utilities

Utilities in Python 3 to read and interpret NMEA sentences from a GPS module ( tested with the NEO-6M ) serially/USB
attached to the Mac.

For more information on GPS/NMEA message formats, see online where there are many great explanations and reference manuals, e.g.:

- https://en.wikipedia.org/wiki/NMEA_0183
- https://www.gpsinformation.org/dale/nmea.htm

See the accompanying video at: https://youtu.be/l_Yh8S8CQ-0

Scripts in this repo:

- messages.py       = listens to the GPS module for a while, then reports on the sentence types seen from the NMEA stream
- location-gga.py   = example of reading $GPGGA and extracting location lat/long and height
- satellites-gsv.py = reports on satellites currently in view by the module (also gives some information on satellite identity )
- time-gga.py       = reads $GPGGA and unpacks the UTC time
- raw_read_gps.py   = output all sequences unfiltered, like using the 'screen' command
- vtg.py            = read the $GPVTG sentences
- gll.py            = read the $GPGLL sentences
- gsa.py            = read the $GPGSA sentences
- rmc.py            = read the $GPRMC sentences


