# Вариант 1
# def my_func(x, y):
#     return(x**y)

# Вариант 1
def my_func(x, y):
    res = 1
    for i in range(0, abs(y)):
        res = res * x
    if y < 0:
        return 1/res
    else:
        return res;

print(my_func(3,-2))
