
def div(n1, n2):
    try:
        res = n1/n2
        return res
    except ZeroDivisionError:
        print('ZeroDivisionError')
        return

a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
print('Частное: ', div(a,b))
