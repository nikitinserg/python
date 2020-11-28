"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, class_date):
        self.class_date = str(class_date)

    @classmethod
    def get_dmy(cls, class_date):
        day, month, year = list(class_date.split('-'))
        return int(day), int(month), int(year)

    @staticmethod
    def validate_dmy(class_date):
        day = Date.get_dmy(class_date)[0]
        month = Date.get_dmy(class_date)[1]
        year = Date.get_dmy(class_date)[2]
        if 1 <= day <= 31:
            print(f'день "{day}" норм')
        else:
            print(f'день "{day}" неправильный (должен быть в интервале от 1 до 31)')
        if 1 <= month <= 12:
            print(f'месяц "{month}" норм')
        else:
            print(f'месяц "{month}" неправильный (должен быть в интервале от 1 до 12)')
        if year < -6984:
            print('Мир сотворён в 6984 году до н.э. Год не может быть меньше этой цифры')
        elif year > 3797:
            print('Конец света наступит в 3797 году. Год не может быть больше этой цифры')
        else:
            print(f'год "{year}" норм')


user_date = input('Введите дату в формате «день-месяц-год»: ')
d = Date(user_date)
Date.validate_dmy(user_date)
print('Результат извлечения числа, месяца, года: ', Date.get_dmy(user_date))