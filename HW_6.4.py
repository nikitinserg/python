"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self. is_police = is_police
    def go(self):
        return f'Автомобиль {self.name} начал движение'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Скорость {self.speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed} км/ч. Превышение скорости!!!'
        else:
            return f'{self.speed} км/ч. Допустимая скорость.'

class SportCar(Car):
    logo = 'Девушки любят спортивные автомобили'

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.speed} км/ч. Превышение скорости!!!'
        else:
            return f'{self.speed} км/ч. Допустимая скорость.'

class PoliceCar(Car):
    is_police = True
    logo = 'Милиция-полиция, нам нужен лишь итог:\nНасильников, грабителей тюремный ждет чертог.\nПолиция-милиция, нам важно лишь одно:\nЧтоб жулики и воры все сели заодно.\n'
    def show_speed(self):
        if self.speed > 60:
            return f'В исключительных случаях полицейские автомобили могут отступать от требований ПДД.\nДаже если их скорость {self.speed} км/ч.'
        else:
            return f'{self.speed} км/ч. Допустимая скорость.'


tc = TownCar(50, 'зеленый', 'ВАЗ-2107', False) # Создаем экземпляр класса-потомка и вызываем его методы
print(tc.go())
print(tc.stop())
print(tc.turn('налево'))
print(tc.show_speed()) # метод show_speed переопределен

sc = SportCar(250, 'красный', 'Ferrari', False) # в SportCar есть своя переменная
print(f'\n{sc.logo}. Особенно, если это {sc.color} {sc.name}\n')

pc = PoliceCar(150, 'серо-синий', 'Lada Kalina', True) # в PoliceCar свой особый метод show_speed
print(f'\n{pc.logo}\n{pc.show_speed()}')


