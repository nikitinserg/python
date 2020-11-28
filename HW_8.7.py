class ComplexDigit:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i'

a_1, b_1 = map(int, input('Введите действительную и мнимую часть \033[1mпервого\033[0m комплексного числа через пробел: ').split())
a_2, b_2 = map(int, input('Введите действительную и мнимую часть \033[1mвторого\033[0m комплексного числа через пробел: ').split())


d_1 = ComplexDigit(a_1, b_1)
d_2 = ComplexDigit(a_2, b_2)
print(f'({a_1} + {b_1}i) + ({a_2} + {b_2}i) = {d_1 + d_2}')
print(f'({a_1} + {b_1}i) * ({a_2} + {b_2}i) = {d_1 * d_2}')