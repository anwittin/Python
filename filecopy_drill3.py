import shutil, os, datetime as DT, time
from datetime import timedelta, datetime

source = "C:\\Folder A\\"
dest = "C:\\Folder B\\"
files = os.listdir(source)
files.sort()
t1 = time.time()


for f in files:
	f[0]
	src = source +f
	f1 = os.path.getmtime(src)
	if t1 - f1 < 86400: 
		dst = dest +f
		shutil.move(src, dst)
		print "File '%s' has changed in the last 24 hours\n moving from %s to %s " %(f, source, dest)
		time.sleep(.75)
	else:
		print "File '%s' has not been modified in last 24 hours" %f
		time.sleep(.5)
	