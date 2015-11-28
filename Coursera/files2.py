# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue 
    line = line.rstrip()
    a = line.find(":")
    num = float(line[a+1:])
    add = num + add
    count = count+1
    avg = add/count

    
print "Average span confidence: ", avg