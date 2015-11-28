fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = list()
for line in fh:
    lst=line.split()
   
    for word in lst:
        if word not in lst2:
            lst2.append(word)
            lst2.sort()
print  lst2
