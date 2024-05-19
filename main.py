import sqlite3
import random

connection = sqlite3.connect("Univercity.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Students'")
result = cursor.fetchone()
if result == None:
    cursor.execute("CREATE TABLE Students(id,family_name,name,age,student_code)")


def insert(id,family_name,name,age,Student_Code):
    cursor.execute("INSERT into Students values(?,?,?,?,?)",(id,family_name,name,age,Student_Code))
    connection.commit()
    connection.close()
def delete(Student_Code):
    cursor.execute("DELETE from Students WHERE Student_Code = ?",(Student_Code,))
    connection.commit()
    connection.close()
def edit(Student_Code):
    cursor = connection.cursor()
    x = input("What do you want to change? :")
    x = x.lower()
    if x == "name":
        newname = input("Please enter your new name :")
        cursor.execute("UPDATE Students SET name = ? WHERE Student_Code = ?",(newname,Student_Code))
    elif x == "age":
        newage = int(input("Please enter your new age :"))
        cursor.execute("UPDATE Students SET age = ? WHERE Student_Code = ?",(newage,Student_Code))
    connection.commit()
    connection.close()

def initialize():
    connection.execute("SELECT Students from sqlite_master WHERE type='table' AND name=?")


while True:
    operation = input("Please enter a correct operation :")
    operation = operation.lower()
    if operation == "insert":
        id = input("Please enter id :")
        family_name = input("Pease enter your family name :")
        name = input("Please enter your name :")
        age = input("Please enter your age :")
        Student_code = random.randint(100_000,999_999)
        print(Student_code)
        insert(id,family_name,name,age,Student_code)
    elif operation == "delete":
        Student_Code = input("Please enter your Student Code :")
        delete(Student_Code)
    elif operation == "edit":
        Student_Code = int(input("Please enter your Student Code :"))
        edit(Student_Code)
    elif operation == "show":
        cursor.execute("SELECT * from Students")
        row = cursor.fetchall()
        for r in row:
            print(r)
    elif operation == "initialize":
        initialize()
    else:
        print("Please enter a correct operation!")

    process = input("Do you want to continue? :")
    process = process.lower()
    if process == "yes":
        continue
    else:
        print("Finished")
        break