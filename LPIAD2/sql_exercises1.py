import sqlite3
# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')
conn.execute("CREATE TABLE SIMPSON_INFO ( \
ID INTEGER PRIMARY KEY AUTOINCREMENT, \
NAME TEXT, \
GENDER TEXT, \
AGE INT, \
OCCUPATION TEXT \
);")

# Add Bart Simpson to the table
conn.execute("INSERT INTO SIMPSON_INFO \
(NAME, GENDER, AGE, OCCUPATION) VALUES \
('Bart Simpson', 'Male', '10', 'Student')");

# Save changes
conn.commit()