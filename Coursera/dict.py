fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()

for line in fh:
    if not line.startswith("From ") : continue 
    l = line.split()[1:2]
    for w in l:
        counts[w] = counts.get(w,0)+1

    bigcount = None
    bigword =  None    
    for word,count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
       
print bigword, bigcount