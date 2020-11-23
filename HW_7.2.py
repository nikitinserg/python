"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        fabric = self.param / 6.5 + 0.5 + 2 * self.param + 0.3
        return f'Объем израсходованной ткани:{fabric}'

    @abstractmethod
    def abstr(self):
        return 'Это абстрактный метод'

class Topcoat(Clothes):
    def consumption(self):
        fabric = 2 * self.param + 0.3
        return f'Для пошива пальто нужно {fabric:.2f} ткани'

    def abstr(self):
        return 'Абстрактный метод класса Пальто'

class Costume(Clothes):
    def consumption(self):
        fabric = self.param / 6.5 + 0.5
        return f'Для пошива костюма нужно {fabric:.2f} ткани'

    def abstr(self):
        return 'Абстрактный метод класса Пальто'


topcoat = Topcoat(100)
costume = Costume(150)
print(topcoat.consumption())
print(costume.consumption())
print(topcoat.abstr())
