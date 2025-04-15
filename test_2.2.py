import sqlite3
class DataManager:
    def __init__(self, db_name = "userss.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS userss(
                id INTEGER PRIMIRY KEY AUTOINCREMENT,
                name TEXT NOT NULL
                role TEXT)
                """)
    def user_info(self, name):
        self.cursor.execute("SELECT * FROM userss WHERE name = ?", (name,))
        y = self.cursor.fetchone()
        print(y)



class User:
    def __init__(self,  name):
        self.name = name
    def new_user(self, user):
        self.cursor.execute("INSERT INTO userss (name) VALUES = ?", (user.name,))
        self.connection.commit()
    def get_user_by_id(self, id):
        self.cursor.execute("SELECT * FROM userss WHERE id = ?", (id,))
        x = self.cursor.fetchone()
        print(x)
    def delete_user_by_id(self, id):
        self.cursor.execute("DELETE FROM userss WHERE id = ?", (id,))
        print(f"Пользователь удален")

class Admin(User):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.role = "Admin"
    def __init__(self, db_name = "admins.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS admins(
                id INTEGER PRIMIRY KEY AUTOINCREMENT,
                name TEXT NOT NULL
                role TEXT)
                """)
    def new_user(self, user):
        self.cursor.execute("INSERT INTO admins (name) VALUES = ?,?", (user.name, user.role))
        self.connection.commit()
    def get_user_by_id(self, id):
        self.cursor.execute("SELECT * FROM admins WHERE id = ?", (id,))
        x = self.cursor.fetchone()
        print(x)
    def delete_user_by_id(self, id):
        self.cursor.execute("DELETE FROM admins WHERE id = ?", (id,))
        print(f"Пользователь удален")






class Customer(User):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.role = "Customer"
    def __init__(self, db_name = "customers.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMIRY KEY AUTOINCREMENT,
                name TEXT NOT NULL
                role TEXT)
                """)
    def new_user(self, user):
        self.cursor.execute("INSERT INTO customers (name) VALUES = ?,?", (user.name, user.role))
        self.connection.commit()
    def get_user_by_id(self, id):
        self.cursor.execute("SELECT * FROM customers WHERE id = ?", (id,))
        x = self.cursor.fetchone()
        print(x)
    def delete_user_by_id(self, id):
        self.cursor.execute("DELETE FROM customers WHERE id = ?", (id,))
        print(f"Пользователь удален")