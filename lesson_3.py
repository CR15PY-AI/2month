# #Принципы ООП: Инкапсуляция и Полиморфизм
# class BankAccount:
#     def __init__(self, balance = 0):
#         self.__balance = balance 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def with_draw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# account.with_draw(200)
# print(account.get_balance())

# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name #открытый
#         self._age = age # защищенный
#         self.__salary = salary #Приватный
# # def get_age(self): #Геттер для защищенного атрибута
# #         return self._age
# #     def set_age(self, age): #CЕттер для защищенного атрибута
# #         if age > 0:
# #             self._age = age 
# #         else:
# #             print("Возраст должен быть положительным")

# #     def get_salary(self):
# #         return self.__salary
# #     def set_salary(self, salary):
# #         if salary >= 0:
# #             self.__salary = salary
# #         else:
# #             print("Зарплата не может быть отрицательной")


#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, value):
#         if value > 0:
#             self._age = value
#         else:
#             raise ValueError("Возраст должен быть положительным")
#     @property
#     def salary(self):
#         return self.__salary
    
#     @salary.setter
#     def salary(self,value):
#         if value > 0:
#             self.__salary = value
#         else:
#             raise ValueError("Зарпалата должна быть положительной")
        

# person = Person(name= "Azamat", age = 60, salary = 100000)

# print("Имя ", person.name)
# print("Возраст до изменения: ", person.age)
# person.age = 45
# print("Возраст после: ", person.age)
# print("ЗП до изменения: ", person.salary)
# person.salary = 120000
# print("ЗП после: ", person.salary)
# # print(person._Person__salary) #Лучше не надо

# class Animal:
#     def speak(self):
#         pass

# class Cat(Animal):
#     def speak(self):
#         return "Мяу"

# class Dog(Animal):
#     def speak(self):
#         return "Гав"

# class Cow(Animal):
#     def speak(self):
#         return "Муу"

# animals = [Cat(), Dog(), Cow()]

# for animal in animals:
#     print(animal.speak())



class Vehicle:
    def move(self):
        raise NotImplementedError("Этот метод должен быть в дочерних классах!!")
    
class Car(Vehicle):
    def move(self):
        return "Авто едет по дороге"
    
class Plane(Vehicle):
    def move(self):
        return "Самолет летит в небе"
    
vehicles = [Car(), Plane()]
for vehicle in vehicles:
    print(vehicle.move())