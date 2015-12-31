# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
btCount = 0
btInitAdd = 0
btFinalAdd = 0
alsCount = 0
alsInitAdd = 0
alsFinalAdd = 0
alsLowPassFailCount = 0
alsHighPassFailCount = 0
for line in fh:
    if line.startswith("<BT >"):
        line = line.rstrip()
        btInit = line.find(",")
        btFinal = line.find(", 1 <")
        btInitNum = float(line[btInit-2:9].strip(","))
        btFinalNum = float(line[btFinal-2:13].strip(","))
        btInitAdd = btInitNum + btInitAdd
        btFinalAdd = btFinalNum + btFinalAdd
        btCount = btCount+1
        btInitAvg = btInitAdd/btCount
        btFinalAvg = btFinalAdd/btCount
    if line.startswith("<ALS>"):
        line = line.rstrip()
        alsInit = line.find(",")
        alsFinal = line.find(", 1 <")
        alsInitNum = float(line[alsInit-2:9].strip(","))
        if alsInitNum > 50.0:
            alsLowPassFailCount += 1
        alsFinalNum = float(line[alsFinal-4:14].strip(","))
        if alsFinalNum < 900.0:
           alsHighPassFailCount += 1
        alsInitAdd = alsInitNum + alsInitAdd
        alsFinalAdd = alsFinalNum + alsFinalAdd
        alsCount = alsCount+1
        alsInitAvg = alsInitAdd/btCount
        alsFinalAvg = alsFinalAdd/btCount
print "\nBoard Test Sample Size: ", btCount
print "<BT_init>: ", btInitAvg
print "<BT_final>: ", btFinalAvg 
print "#########################"
print "\nALS Sample Size: ", alsCount
print "<ALS_init>: ", alsInitAvg
print "<ALS_final>: ", alsFinalAvg
print "<ALS_Low_Pass_Fail>: ", alsLowPassFailCount
print "<ALS_High_Pass_Fail>: ", alsHighPassFailCount

