"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, mass_of_sqr_m, thickness):
        return self._length * self._width * mass_of_sqr_m * thickness

    # def area(self):
    #     return self._length * self._width

lenght = float(input('Длина дороги (м): '))
width = float(input('Ширина дороги (м): '))
mass_of_sqr_m = float(input('Масса одного кв метра асфальта толщиной 1см (кг): '))
thickness = float(input('Толщина асфальта (см): '))

asf = Road(lenght, width)
print(f'Масса асфальта составит {asf.weight(mass_of_sqr_m, thickness)} кг.')
# print(f'Площадь асфальта: {asf.area()} кв.м.')