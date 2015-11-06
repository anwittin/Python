import datetime as DT
from datetime import datetime, timedelta
import time

# establish the times for each location
t1 = DT.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
t2 = DT.datetime.fromtimestamp(time.time()) + timedelta(hours=3)
t3 = datetime.now() + timedelta(hours=8)
print "The time in Portland is: %s." % t1
# New York time check
estpm = t2.replace(hour=21, minute=0, second=0)
estam = t2.replace(hour=9, minute=0, second=0)
if t2 > estpm or t2 < estam:
    print "The time in New York is: %s.\nNew York branch is closed" % t2.strftime('%H:%M:%S')
else:
    print "The time in New York is: %s.\nThe New York branch is open" % t2.strftime('%H:%M:%S')
    # London time check
gmtpm = t3.replace(hour=21, minute=0, second=0)
gmtam = t3.replace(hour=9, minute=0, second=0)
if t3 > gmtpm or t3 < gmtam:
    print "The time in London is: %s.\nLondon branch is closed" % t3.strftime('%H:%M:%S')
else:
    print "The time in London is: %s.\nThe London Branch is Open" % t3.strftime('%H:%M:%S')

