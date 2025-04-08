#ООП - Наследование
# class Game: #Родительский класс
#     def __init__(self, name, game_year, company, grafic):
#         self.name = name
#         self.game_year = game_year
#         self.company = company
#         self.grafic = grafic
#     def info(self):
#         print(f"Game - {self.name} - {self.game_year} - {self.company} - {self.grafic}")
# game = Game("Mortal Combat", 2014, "Midway Games", "4K")
# game.info()

# class Roblox(Game):
#     def __init__(self, name, game_year, company, grafic, multiplayer):
#         super().__init__(name, game_year, company, grafic)
#         #Game.__init__(name, game_year, company, grafic) #Тоже самое но обращение напрямую к классу
#         self.multiplayer = multiplayer
#         self.login = "player"
#         self.gender = "None"
#         self.skin = "None"
#         self.HP  = 100
#     def info_player(self):
#         print(f"Игрок - {self.login} \nПол - {self.gender}\nОблик - {self.skin}\nЗдоровье - {self.HP}")

#     def edit_player(self):
#             login = input("Введите свое имя")
#             gender = input("Введите свой пол")
#             skin = input("Введите свой облик")
#             self.login = login
#             self.gender = gender
#             self.skin = skin

#     def info(self):
#         return super().info()
# roblox = Roblox("Roblox", 2006, "Roblox.corp", "Full HD", 8)
# roblox.info()
# roblox.edit_player()
# roblox.info_player()
# class Strike(Roblox):
#     def __init__(self, name, game_year, company, grafic, multiplayer):
#         super().__init__(name, game_year, company, grafic, multiplayer)
#     def info(self):
#         return super().info()
#     def info_player(self):
#         return super().info_player()
#     def edit_player(self):
#         return super().edit_player()
# strike = Strike("1234", "1234", "1234", "12345", 999)
# strike.info()
# strike.edit_player()
# strike.info_player()



#ZOO
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} ест")
    def sleep(self):
        print(f"{self.name} спит")

class Walker(Animal):
    def __init__(self, name):
        super().__init__(name)
    def walk(self):
        print(f"{self.name} ходит")
walker = Walker()

class Swimer(Animal):
    def __init__(self, name):
        super().__init__(name)
    def swim(self):
        print(f"{self.name} плавает")

class Flyer(Animal):
    def __init__(self, name):
        super().__init__(name)
    def fly(self):
        print(f"{self.name} летает")


class Penguin(Walker, Swimer):
    def __init__(self, name):
        super().__init__(name)
    def describe(self):
        self.walk()
        self.swim()

class Duck(Walker, Swimer, Flyer):
    def __init__(self, name):
        super().__init__(name)
    def describe(self):
        self.walk
        self.swim()
        self.fly()

class Bat(Flyer):
    def __init__(self, name):
        super().__init__(name)
    def describe(self):
        self.fly()
    
animal = Animal("Медведь")
animal.eat()
animal.sleep()
penguin = Penguin("Пингвин")
bat = Bat("Летучая Мышь")
duck = Duck("Утка")
penguin.describe()
bat.describe()
duck.describe()
