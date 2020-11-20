"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep

class TrafficLight:

    def __init__(self, colors = {'rojo': 7, 'amarillo': 2, 'verde':7}):
        self._colors = colors

    def running(self):
        for c, t in self._colors.items():
            print(f'Цвет: {c}, Длительность: {t} сек.')
            sleep(t)

colors_ru = {'красный': 7, 'желтый': 2, 'зеленый':7}
# colors_en = {'red': 7, 'yellow': 2, 'green':7}
# colors_xx = {'red': 3, 'yellow': 2, 'green':3, 'blue': 1, 'white': 3}

t_ru = TrafficLight(colors_ru)
t_ru.running()

# t_en = TrafficLight(colors_en)
# t_en.running()
#
# t_xx = TrafficLight(colors_xx)
# t_xx.running()
# 
# t_es = TrafficLight()
# t_es.running()




