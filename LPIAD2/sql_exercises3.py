import sqlite3
# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Get data from the db

cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME = 'Homer Simpson'")
cursor = conn.execute("SELECT * from SIMPSON_INFO where GENDER = 'Male'")

# Get data from cursor

rows = cursor.fetchall()
print rows
