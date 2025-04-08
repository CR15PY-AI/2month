class Transport:
    def __init__(self):
        self._speed = 0

    def move(self):
        print("Транспорт начал движение.")
    def set_speed(self, speed):
        if speed >= 0:
            self._speed = speed
        else:
            print("Скорость не может быть отрицательной.")
    def get_speed(self):
        return self._speed


class Car(Transport):
    def move(self):
        print("Автомобиль едет по дороге.")
class Bicycle(Transport):
    def move(self):
        print("Велосипед катится по велодорожке.")

transport_list = [Car(), Bicycle()]

transport_list[0].set_speed(60)
transport_list[1].set_speed(20)

for transport in transport_list:
    transport.move()
    print(f"Скорость: {transport.get_speed()} км/ч\n")