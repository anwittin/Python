import sqlite3
# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Delete the extra character
conn.execute("DELETE from SIMPSON_INFO where ID = 2")

# Save changes
conn.commit()

# Prints the number of changes to the database

changes = conn.total_changes
print "Number of changes: ", changes

cursor = conn.execute("SELECT * from SIMPSON_INFO")

# Get data from cursor

rows = cursor.fetchall()
print rows
