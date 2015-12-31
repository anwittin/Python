import re
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
for line in fh:
    line = line.rstrip()
    sum = re.findall('[0-9]+', line)
    sum = [int(x) for x in sum]
    if len(sum) > 0:
        for i in sum:
            total = total +i
print total