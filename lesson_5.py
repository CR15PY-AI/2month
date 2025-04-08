import sqlite3
connect = sqlite3.connect("users2.db")
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS users2(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL
        )
""")

def register():
    name = input("Введите ФИО: ")
    cursor.execute(f"""INSERT INTO users2
                   (name) 
                   VALUES (?)""" ,(name,))
    connect.commit()

def all_users():
    cursor.execute("SELECT * FROM users2")
    students = cursor.fetchall()
    print(students)


register()
all_users()