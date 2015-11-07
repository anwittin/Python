import shutil
import os, time


dest = "C:\\Users\\tonywittingerllc\\Desktop\\Folder B\\"
source = "C:\\Users\\tonywittingerllc\\Desktop\\Folder A\\"
files = os.listdir(source)
files.sort()

for f in files:
	src = source +f
	dst = dest +f
	shutil.move(src, dst)
	print "Moved file: %s from %s to %s " %(f, source, dest)


