"""ООП - Обьектно Ориентированное Програмирование"""
#Классы
# class Car: #Шаблон или чертеж
#     def __init__(self, motor, wheel, body): #__init__ это конструктор
#         self.motor = motor # self - ссылка на текущий обьект
#         self.wheel = wheel
#         self.body = body # Атрибут класса

#         self.bak = 10 #Атрибут метода
#         self.is_start = False #Флажок

#     def info(self): #Функции в классах превращаются в методы
#         print(f"Мотор - {self.motor}, Колесо - {self.wheel}, Кузов - {self.body}")

#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print("Машина заведена")
#         else:
#             print("У машины нет топлива")
    
#     def stop(self):
#         self.is_start == False
#         print("Машина заглушена")

#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Машина едет в {city}")
#         else:
#             print("Машина не заведена")
        
# car = Car("V6", "R20", "Sky") #Экзеспляр класса
# car.info()
# car.start()
# car.drive("Дубай")

class Book:
    def __init__(self, avtor, book_name, year):
        self.avtor = avtor
        self.book_name = book_name
        self.year = year
    def info(self):
        print(f"Автор - {self.avtor}, Название - {self.book_name}, Год выпуска - {self.year}")
book = Book("Достоевский", "Преступление и Наказание", "1866")
book.info() 