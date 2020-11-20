"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        return (f'{self.surname} {self.name}')

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

name = 'Петр'
surname = 'Иванов'
position = 'менеджер'
income = {'wage': 10000, 'bonus': 5000}

w_1 = Position(name, surname, position, income)
print(f'полное имя: {w_1.get_full_name()}. Зарплата: {w_1.get_total_income()}')

# name = 'Иван'
# surname = 'Петров'
# position = 'специалист 1 категории'
# income = {'wage': 9000, 'bonus': 4000}
#
# w_2 = Position(name, surname, position, income)
# print(f'полное имя: {w_2.get_full_name()}. Зарплата: {w_2.get_total_income()}')