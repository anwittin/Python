# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("<BT >") : continue 
    line = line.rstrip()
    print line
    a = line.find("> ")
    print a
    num = int(line[a+1:3])
    print num
    # add = num + add
    # print add
    # count = count+1
    # print count
    # avg = add/count
    # print avg
    
# print "Average spam confidence: ", avg