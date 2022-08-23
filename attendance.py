import sqlite3
connection = sqlite3.connect("IITK.db")

cursor = connection.cursor()

sql_command = ''' 
CREATE TABLE attendance ( 
roll_no INTEGER, 
firstname VARCHAR(20), 
lastname VARCHAR(30), 
day DATE,
att CHAR(1) );'''

cursor.execute(sql_command)