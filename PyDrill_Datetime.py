import datetime
import time

# get and print out the date and time for:
# portland oregon, london, uk and new york,
# check the time v. portland if branch is 
# open or closed. 

# work off PST adjust for EST and GMT
# use datetime to get proper output
# timedelta, tzinfo will be the main objects used

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

# Usage demo1:
print todayAt (17), todayAt (17, 15)

# Usage demo2:    
timeNow = datetime.datetime.now()
if timeNow < todayAt (13):
   print "Too Early"