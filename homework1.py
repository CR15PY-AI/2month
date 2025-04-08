#1
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        print(f"Привет! Меня зовут {self.name} , мне {self.age} лет, я живу в городе {self.city}")
person1 = Person("Азамат", "18", "Ош")
person2 = Person("Kaiser", "21", "Frankfurt")
person1.introduce()
person2.introduce()

#2
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        print(f"Автомобиль: {self.brand} {self.model} {self.year} года")
car = Car("Tesla", "Model X", "2020")
car.info()

#3
class BankAccount:
        def __init__(self, owner, balance = 0):
            self.owner = owner
            self.balance = balance
        def deposit(self, amount: int):
            self.balance += amount
            return self.balance
        def withdraw(self, amount: int):
            if self.balance >= amount:
                self.balance -= amount  
                return self.balance
            else:
                print("Недостаточно средств на счете")
        def show_balance(self):
            print(f"{self.owner}: {self.balance} Сом")
bankaccount = BankAccount("azamat", 10000)
# bankaccount.deposit(100)
bankaccount.withdraw(400)
bankaccount.show_balance()