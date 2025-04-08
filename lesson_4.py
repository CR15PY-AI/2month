#ООП  - АБСТРАКЦИЯ

# class Programmer:
#     def direction(self):
#         pass
#     def language(self):
#         pass
#     def laptop(self):
#         pass

# class WebDeveloper(Programmer):
#     def direction(self):
#         return f"Backend"
#     def language(self):
#         return f"Python"
#     def laptop(self):
#         return f"True"
    
# class Vercerl(Programmer):
#     def direction(self):
#         return f"Frontend"
#     def language(self):
#         return f"JavaScript"
#     def laptop(self):
#         return f"False"
    
# class Server(Programmer):
#     def direction(self):
#         return f"Devops"
#     def language(self):
#         return f"Linux/Python"
#     def laptop(self):
#         return f"True"
    

# programmer = [WebDeveloper(), Vercerl(), Server()]

# for i in programmer:
#     print(i.direction())
#     print(i.language())
#     print(i.laptop())


# class Transport:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def info(self):
#         return f"{self.brand}, {self.speed}"
#     def move(self):
#         print("Транспорт движется")

# class Car(Transport):
#     def move(self):
#         return f"Машина едет по дороге"
#     def honk(self):
#         print("Машина сигналит")

# class Bicycle(Transport):
#     def move(self):
#         return f"Велосипед едет по тропинке"
#     def ring_bell(self):
#         print("Велосипед звенит звонком")


# class Airplane(Transport):
#     def move(self):
#         return f"Самолет летит в небе"
#     def take_off(self):
#         print("Самолет взлетает")




# car = Car("Lexus", "60mph")
# bicycle = Bicycle("speedster", "14mph")
# airplane = Airplane("AirBus", "400mph")



# transport = [car, bicycle, airplane]
# for i in transport:
#     print(i.info())
# for i in transport:
#     print(i.move())


# car.honk()
# bicycle.ring_bell()
# airplane.take_off()


#БД - Базы Данных
#CУБД - система управления базы данных

import sqlite3
connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            age INT DEFAULT NULL,
            direction TEXT, 
            is_have BOOLEAN NOT NULL DEFAULT FALSE,
            birth_date DATE,
            rating DOUBLE (4,2) DEFAULT (0.0)
        )
""")

def register():
    full_name = input("Введите ФИО: ")
    age = int(input("Введите свой возраст: "))
    direction = input("Введите ваше направление: ")
    is_have = bool(input("наличие ноутбука: "))
    birth_date = input("Введите дату рождения: ")
    rating = float(input("Введите свой рейтинг: "))

    # cursor.execute(f"""INSERT INTO users
    #                (full_name, age, direction, is_have, birth_date, rating) 
    #                VALUES ("{full_name}", {age}, '{direction}', {is_have}, '{birth_date}', {rating})""")
    
    # connect.commit() #Сохранение в БД


    cursor.execute(f"""INSERT INTO users
                   (full_name, age, direction, is_have, birth_date, rating) 
                   VALUES (?,?,?,?,?,?)""" ,(full_name, age, direction, is_have, birth_date, rating))
#Плейсхолдер (англ. placeholder) — это специальный символ или текстовый маркер, который используется в SQL-запросах и других контекстах программирования для обозначения места, куда позже будет вставлено значение
    connect.commit() #Сохранение в БД
def all_students():
    cursor.execute("SELECT * FROM users")
    students = cursor.fetchall()
    print(students)

def one_student(id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    students = cursor.fetchone()
    print(students)

def delete_student(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()
    print(f"Пользователь {id}, был успешно удален")
# register()
# all_students()
# one_student(2)
delete_student(2)
# INTEGER - int
# VARCHAR - str
# DOUBLE - float
# 



