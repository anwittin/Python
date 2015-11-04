__author__ = 'tonywittingerllc'

import sqlite3

firstName = raw_input("Enter your first name: ")
lastName = raw_input("Enter your last name: ")
age = int(raw_input("Enter your age: "))

personData = (firstName, lastName, age)
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
c.execute("INSERT INTO People VALUES(?,?,?)", personData)

print(personData)