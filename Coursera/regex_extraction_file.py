'''This is a file that will be used to extract data from a python program to add
to a list that can then be used in a js file as an array. I am using regex to try
shorten the code and make the file more dynamic'''

'''Regex guide:
^	Matches the beginning of a line				
$	Matches the end of the line				
.	Matches any character				
\s	Matches whitespace				
\S	Matches any non-whitespace character				
*	Repeats a character zero or more times				
*?	Repeats a character zero or more times (non-greedy)				
+	Repeats a character one or more times				
+?	Repeats a character one or more times (non-greedy)				
[aeiou]	Matches a single character in the listed set				
[^XYZ]	Matches a single character not in the listed set				
[a-z0-9]	The set of characters can include a range				
(	Indicates where string extraction is to start				
)	Indicates where string extraction is to end				
'''
import re
fname = raw_input("Enter file name: ")
fh = open(fname)
funcName = []
optionOne = []
optionTwo = []
choiceOne = []
choiceTwo = []


# for line in fh:
    # if line.startswith("def"):
        # line = line.rstrip()
        # funcName = re.findall('/S[^a-z]+?', line)
        # print funcName
            #if len(funcName) > 0:
                #print funcName
        # btFinal = line.find(", 1 <")
        # btInitNum = float(line[btInit-2:9].strip(","))
        # btFinalNum = float(line[btFinal-2:13].strip(","))
        # btInitAdd = btInitNum + btInitAdd
        # btFinalAdd = btFinalNum + btFinalAdd
        # btCount = btCount+1
        # btInitAvg = btInitAdd/btCount
        # btFinalAvg = btFinalAdd/btCount


for line in fh:
    line = line.rstrip()
    sum = re.search('^def', line)
    #sum = [int(x) for x in sum]
    #if len(sum) > 0:
    print sum
        # # for i in sum:
            # # total = total +i
#print total