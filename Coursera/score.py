score = raw_input("Enter a score between 0.0 and 1.0:")

try:
    grade = float(score)
except: 
    print "Enter a number only"
if grade > 1.0:
    print "Please enter a number between 0.0 and 1.0"
elif grade < 0.0:
    print "Please enter a positive number"
elif grade >= 0.9: 
    print "A"
elif grade >= 0.8:
    print "B"
elif grade >= 0.7:
    print "C"
elif grade >= 0.6:
    print "D"
elif grade < 0.6:
    print "F"
