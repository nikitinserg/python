"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

class Store:

    def __init__(self, name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name}, цена {self.price}руб/шт, количество {self.quantity}шт.'

    def to_store(self):
        try:
            unit_name, unit_price, unit_quantity = input(f'Введите наименование, цену за 1шт и количество через запятую: ').split(',')
            unit = {'Модель устройства': unit_name, 'Цена за 1шт': unit_price, 'Количество': unit_quantity}
            self.my_unit.update(unit)
            self.my_store.append(self.my_unit)
            print(f'Текущий список:\n{self.my_store}')
        except:
            return f'Некорректный ввод. Надо ввести наименование, цену за 1шт и количество через запятую\nПример: "HP LJ 2015,10000,2"'

        q = input(f'Для выхода введите "Q", для продолжения нажмите Enter на пустой строке').lower()
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'В данный момент на складе:\n{self.my_store_full}')
            return f'Ввод закончен'
        else:
            return Store.to_store(self)


class Printer(Store):
    def printing(self):
        return f'Принтер печатает'


class Scaner(Store):
    def scaning(self):
        return f'Сканер сканирует'


class Copier(Store):
    def copying(self):
        return f'Ксерокс копирует'


unit_1 = Printer('hp lj 1320', 10000, 2)
unit_2 = Scaner('Canon lide 410', 5000, 2)
unit_3 = Copier('Xerox fc 108', 7500, 1)
print(unit_1.to_store())
print(unit_2.to_store())
print(unit_3.to_store())
print('Вызов метода принтера unit_1: ', unit_1.printing())
print('Вызов метода сканера unit_2: ',unit_1.scaning())
print('Вызов метода ксерокса unit_3: ',unit_1.copying())