fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
sent = dict()

for line in fh:
    if not line.startswith("From ") : continue 
    l = line.split()
    
    print l
    for w in l:
        sent[w] = 1
    else:
        sent[w] += 1
    
print sent