import os
# The path to the script
currentPath = os.path.dirname( os.path.abspath(__file__))
print currentPath
# Make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv