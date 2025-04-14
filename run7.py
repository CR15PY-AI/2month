from main7 import User, UserService

user = UserService()
user_services = User(name = "KAISER", email = "a.azama2007@mail.ru", age = 18)
user.add_user(user_services)

find = user.find_user_by_email("a.azama2007@mail.ru")
if find:
    print(f"Пользователь найден: {find.name}, {find.email}, {find.age}")

delete = user.delete_user_by_email("a.azama2007@mail.ru")