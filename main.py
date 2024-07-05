import os
import sqlite3
import random

db_path = "Univercity.db"
connection = sqlite3.connect("Univercity.db")
cursor = connection.cursor()

try:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name
        FROM sqlite_master 
        WHERE type='table' AND name=(?);
    """, ("Students",))
    result = cursor.fetchone()
    if result:
        pass
    else:
        cursor.execute("CREATE TABLE Students(id,family_name,name,age,student_code)")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

def insert_user(id,family_name,name,age,Student_Code):
    table_name = "Students"
    cursor.execute("INSERT into Students values(?,?,?,?,?)",(id,family_name,name,age,Student_Code))
    connection.commit()
    
def insert_course(id,math_score,geography_score,Student_code):
    table_name = "Courses"
    cursor.execute("INSERT into Courses values(?,?,?,?)",(id,math_score,geography_score,Student_code))
    connection.commit()
    
def delete_user():
    cursor.execute('SELECT * FROM Students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    name = input("Please Enter desired name: ")
    cursor.execute('DELETE FROM Students WHERE name= ?', (name,))
    connection.commit()
    
def delete_Courses(Student_Code):
    table_name = "Courses"
    cursor.execute("DELETE from Courses WHERE Student_Code = ?",(Student_Code))
    connection.commit()
    
def edit_Students(Student_Code):
    cursor = connection.cursor()
    x = input("What do you want to change? :")
    x = x.lower()
    if x == "family_name":
        newfname = input("Please enter your new family_name: ")
        cursor.execute("UPDATE Students SET family_name = ? WHERE Student_Code = ?",(newfname,Student_Code))
    elif x == "name":
        newname = input("Please enter your new name :")
        cursor.execute("UPDATE Students SET name = ? WHERE Student_Code = ?",(newname,Student_Code))
    elif x == "age":
        newage = int(input("Please enter your new age :"))
        cursor.execute("UPDATE Students SET age = ? WHERE Student_Code = ?",(newage,Student_Code))
    connection.commit()
    
def edit_Courses(Students_Code):
    cursor = connection.cursor()
    x = input("What do you want to change? :")
    x = x.lower()
    if x == "math_score":
        new_math_score = int(input("Please enter your new math score :"))
        cursor.execute("UPDATE Students SET math_score = ? WHERE Student_Code = ?",(new_math_score,Student_Code))
    elif x == "geography_score":
        new_geography_score = int(input("Please enter your new geography score :"))
        cursor.execute("UPDATE Students SET math_score = ? WHERE Student_Code = ?",(new_geography_score,Student_Code))
    else:
        print("ERROR!Please enter a valid data.")
    connection.commit()
    
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
        insert_user(id,family_name,name,age,Student_code)
    elif operation == "insert_course":
        id = input("Please enter id :")
        math_score = input("Please enter math_score: ")
        geography_score = input("Please enter geography_score: ")
        Student_code = int(input("Please enter your Student_Code: "))
        insert_course(id,math_score,geography_score,Student_code)
    elif operation == "delete_user":
        delete_user()
    elif operation == "delete_courses":
        delete_Courses(Student_Code)
    elif operation == "edit_students":
        Student_Code = int(input("Please enter your Student Code :"))
        edit_Students(Student_Code)
    elif operation == "edit_courses":
        Student_Code = int(input("Please enter your Student Code :"))
        edit_Courses(Student_Code)
    elif operation == "show_students":
        row = cursor.execute("SELECT * from Students")
        for r in row:
            print(r)
    elif operation == "show_courses":
        row = cursor.execute("SELECT * from Courses")
        for r in row:
            print(r)
    else:
        print("Please enter a correct operation!")

    process = input("Do you want to continue? :")
    process = process.lower()
    if process == "yes":
        continue
    else:
        print("Finished")
        connection.close()
        break