import sqlite3

# Connect to filecopy database
conn = sqlite3.connect('filecopy.db')

def createTable():
	conn.execute("CREATE TABLE if not exists \
			FILECOPY_INFO( \
			ID INTEGER PRIMARY KEY AUTOINCREMENT, \
			DATETIME_1 INTEGER, \
			DATETIME_2 INTEGER, \
			FILE TEXT, \
			LOCATION TEXT \
			);")
			
			
			
createTable()