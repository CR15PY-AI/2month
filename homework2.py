class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        return f"Транспорт - {self.brand}, Модель - {self.model}, Год - {self.year}"
    def start_engine(self):
        print("Двигатель запущен")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    def info(self):
        print(f"{super().info()} ,{self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type
    def info(self):
        print(f"{super().info()}, {self.type}")

car = Car("Lexus", "RX350", 2018, 4)
bike = Bike("ИЖ", "Планета спорт", 1987, "Унибайк")

car.info()
bike.info()
car.start_engine()
bike.start_engine()