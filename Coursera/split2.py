fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
sent = dict()

for line in fh:
    if not line.startswith("From ") : continue 
    l = line.split()
    l = sent[]
    count = count+1
    
print "There were", count, "lines in the file with From as the first word"