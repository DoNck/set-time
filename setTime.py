#!/usr/bin/python

import urllib2
from datetime import datetime
from dateutil import tz
import os
import ssl

lines=urllib2.urlopen("https://developer.yahoo.com/util/timeservice/V1/getTime.html", context=ssl._https_verify_certificates(False)).readlines()
dateline=lines[-1]
#print dateline

#parse the date from the response:
from_zone=dateline.split()[6]
year=dateline.split()[7]
month=dateline.split()[3]
day=dateline.split()[4]
time=dateline.split()[5]
hours=time.split(':')[0]
mins=time.split(':')[1]
secs=time.split(':')[2]

#print "%s %s %s - %s:%s:%s" % (day,month,year,hours,mins,secs)

# pass the tzinfo option:
# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/datetime.html#datetime.tzinfo
date = datetime.strptime(year + " " + month + " " + day + " " + hours + ":" + mins + ":" + secs, "%Y %b %d %H:%M:%S")
date = date.replace(tzinfo=tz.gettz(from_zone))

to_zone = tz.gettz('Europe/Paris')
local = date.astimezone(to_zone)

#print from_zone+": "+str(date)
#print "local: "+str(local)

# date -s "2 OCT 2006 18:00:00"
print local.strftime("%d %b %Y %H:%M:%S")

command = "date -s '"+local.strftime("%d %b %Y %H:%M:%S"+"'")
print "command: "+command

os.system(command)
