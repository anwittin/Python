import shutil, os, datetime, time

#import Filecopy_drill


source = "C:\\Folder A\\"
dest = "C:\\Folder B\\"
files = os.listdir(source)
files.sort()

for f in files:

	src = source +f
	dst = dest +f

	shutil.move(src, dst)
	print "Moved file: %s from %s to %s " %(f, source, dest)


