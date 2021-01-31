class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed=40):
        self.speed = speed
        print(f'{self.name} поехал')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился')

    def turn_left(self):
        print(f'{self.name} повернул налево')

    def turn_right(self):
        print(f'{self.name} повернул направо')

    def show_speed(self):
        print(f'Текущаа скорость {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущаа скорость {self.name}: {self.speed}')
        if self.speed > 60:
            print(f'{self.name} превысил разрешенную скорость!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущаа скорость {self.name}: {self.speed}')
        if self.speed > 40:
            print(f'{self.name} превысил разрешенную скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(58, 'Черный', 'Volvo S60', False)
car_2 = WorkCar(41, 'Синий', 'Ford Transit', False)
car_3 = PoliceCar(80, 'Белый', 'Ford Mondeo', True)
print(f'{car_1.name} {car_1.color}, скорость {car_1.speed}')
car_1.speed = 90
car_1.show_speed()
car_1.turn_left()
car_1.stop()
car_1.show_speed()
car_1.go()
car_1.show_speed()
print(f'{car_1.name} полицейская машина: {car_1.is_police}')
car_2.show_speed()
