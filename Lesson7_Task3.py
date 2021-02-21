class Cell:
    def __init__(self, quant):
        self.quant = quant

    def __add__(self, other):
        return Cell(self.quant + other.quant)

    def __sub__(self, other):
        if self.quant > other.quant:
            return Cell(self.quant - other.quant)
        else:
            print('Вычитание невозможно')
            return self

    def __mul__(self, other):
        return Cell(self.quant * other.quant)

    def __truediv__(self, other):
        return Cell(self.quant // other.quant)

    def __str__(self):
        return str(self.quant)

    def make_order(self, cols):
        r = self.quant // cols
        d = self.quant % cols
        return  (('*' * cols + '\n') * r) + '*' * d + '\n'

c1 = Cell(20)
c2 = Cell(3)
c3 = c1 + c2
print(c3)
c3 = c1 - c2
print(c3)
c3 = c2 - c1
print(c3)
c3 = c1 * c2
print(c3)
c3 = c1 / c2
print(c3)

print(c1.make_order(7))


