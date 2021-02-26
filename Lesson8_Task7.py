# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex():
    def __init__(self, r, i):
        self.re = r
        self.im = i

    def __str__(self):
        return str(self.re) + str('+' if self.im >= 0 else '') + str(self.im) + 'i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re*other.re - self.im * other.im, self.re*other.im + self.im*other.re)
        else:
            return None

ya = Complex(2,3)
print(ya)

vu = Complex(6,-5)
print(vu)

print(ya + vu)
print(ya * vu)




