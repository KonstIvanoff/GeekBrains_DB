# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, dtstr):
        self.dtstr = dtstr

    @classmethod
    def parse(cls, dt):
        return [int(i) for i in dt.split('-')]

    @staticmethod
    def validate(arr):
        d,m,y = map(lambda x:x, list(arr))

        if len(str(y)) != 4:
            return False
        if m < 1 or m > 12:
            return  False

        if m in (1, 3, 5, 7, 8, 10, 12):
            k = 31
        elif m in (4,6,9,11):
            k = 30
        else:
            if y % 4 == 0:
                k = 29
            else:
                k = 28

        if d >= 1 and d <= k:
            return True
        else:
            return False

p = Date.parse('33-08-1918')
print(p)
r = Date.validate(p)
print(r)

p = Date.parse('29-02-2021')
print(p)
r = Date.validate(p)
print(r)

p = Date.parse('28-02-2021')
print(p)
r = Date.validate(p)
print(r)