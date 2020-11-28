"""
оздайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivByZeroExeption(Exception):
    def __init__(self, text):
        self.text = text


a, b = map(int,input('Введите делимое и делитель через пробел: ').split())

try:
    if b == 0:
        raise DivByZeroExeption('делить на ноль нельзя!')
except DivByZeroExeption as d:
    print(d)
else:
    print(f'{a} / {b} = {a / b}')