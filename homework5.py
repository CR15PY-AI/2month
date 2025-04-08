import sqlite3
connect = sqlite3.connect("orders.db")
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            product TEXT,
            quantity INTEGER
        )
""")

def register():
    name = input("Введите свое ИМЯ: ")
    product = input("Введите название товара: ")
    quantity = int(input("Введите количество товара: "))

    cursor.execute(f"""INSERT INTO orders
                   (name, product, quantity) 
                   VALUES (?,?,?)""" ,(name, product, quantity))
    connect.commit()
    print("Заказ добавлен!")
def all_orders():
    cursor.execute("SELECT * FROM orders")
    x = cursor.fetchall()
    print(x)

def change(x, value):
    cursor.execute("UPDATE orders SET quantity = ? WHERE id = ?", (value, x))

def delete(name):
    cursor.execute("DELETE FROM orders WHERE name = ?", (name,))

def more_1():
    cursor.execute("SELECT * FROM orders WHERE quantity >= 1")
    for i in cursor.fetchall():
        print(i)


# register()
# register()
# register()
# all_orders()
# change(1,5)
# all_orders()
# more_1()
# delete("CR15PY")
# all_orders()