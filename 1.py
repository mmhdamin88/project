import sqlite3

connection = sqlite3.connect("Univercity.db")
cursor = connection.cursor()
x = input("Enter your name :")
y = input("Enter your age :")
# cursor.execute("CREATE TABLE Students(id, name, age, student_code)")
cursor.execute("INSERT into Students values(?,?,?,?)",(1,x,y,1))
connection.commit()
connection.close()