#mysql connector
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="King#123", database ="org")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

mycursor.execute("SELECT * FROM Worker WHERE DEPARTMENT = 'AI/ML'")
print(mycursor.fetchone())

#SQLite
import sqlite3

conn = sqlite3.connect("temp1.db")

cursor = conn.cursor()


cursor.execute(''' 
        Create Table IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(25),
            age INT
            );
''')

cursor.execute('''
        INSERT INTO student (name, age) 
        Values ('Ram', 15),
               ('Shyam', 16);
''')

conn.commit()

cursor.execute('''SELECT * FROM student;''')
result = cursor.fetchall()

print(result)

conn.close()