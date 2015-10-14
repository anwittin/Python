import sqlite3
# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Add Bart Simpson to the table
#conn.execute("INSERT INTO SIMPSON_INFO \
#(NAME, GENDER, AGE, OCCUPATION) VALUES \
#('Bart Simpson', 'Male', '10', 'Student')");

# Add Homer Simpson to the table
conn.execute("INSERT INTO SIMPSON_INFO \
(NAME, GENDER, AGE, OCCUPATION) VALUES \
('Homer Simpson', 'Male', '40', 'Nuclear Plant')");

# Add Lisa Simpson to the table
conn.execute("INSERT INTO SIMPSON_INFO \
(NAME, GENDER, AGE, OCCUPATION) VALUES \
('Lisa Simpson', 'Female', '8', 'Student')");

# Save changes
conn.commit()

# Prints the number of changes to the database

changes = conn.total_changes
print "Number of changes: ", changes