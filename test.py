# import sqlite3
# import os
# path = "test.db"
# isExisting = os.path.exists("./test.db")
# print(isExisting)

# connection = sqlite3.connect("test.db")
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE name(i)")

# cursor = connection.cursor()
# cursor.execute("""
#     SELECT name
#     FROM sqlite_master 
#     WHERE type='table' AND name=?;
# """, ("name",))
# result = cursor.fetchone()
# print(result)
# if result == None:
#    print("create in table")
#    cursor.execute("CREATE TABLE name(i)")
# else:
#     print("show in table")
#     x = cursor.execute("SELECT * from name")
#     for i in x:
#         print(i)
# cursor.close()
# connection.close()


import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    )
''')
users = [
    ("Alice", 30, "alice@example.com"),
    ("Bob", 24, "bob@example.com"),
    ("Charlie", 29, "charlie@example.com")
]
cursor.executemany('''
    INSERT INTO users (name, age, email)
    VALUES (?, ?, ?)
''', users)

# Commit the transaction
connection.commit()
def display_users():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

display_users()

cursor.execute('DELETE FROM users WHERE name= ?', ('Bob',))
display_users()