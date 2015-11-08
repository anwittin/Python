import shutil, os, time
import datetime as DT
from datetime import datetime, timedelta


source = "C:\\Users\\tonywittingerllc\\Desktop\\Folder A\\"
dest = "C:\\Users\\tonywittingerllc\\Desktop\\Folder B\\"
files = os.listdir(source)
files.sort()
def fileCopy():
	for f in files:
		if 
		src = source +f
		dst = dest +f
		shutil.move(src, dst)
		print "Moved file: %s from %s to %s " %(f, source, dest)


