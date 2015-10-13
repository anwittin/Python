from sys import argv
# requrired input for the argument
script, filename = argv

# Print the statements for what we will be doing
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

# Input symbol for the user to make choice
raw_input("?")

# using the open function to open the argv filename
print "Opening the file..."
target = open(filename, 'w')

# using the truncate function to remove the data

print "Truncating the file. Goodbye!"
target.truncate()

# Ask user for the new input for the file

print "Now I'm going to ask you for three lines."

# The replacement lines in the text

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to file."
# taking the input and placing it in the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

#Closing the file
target.close()

