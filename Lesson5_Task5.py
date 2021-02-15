import random

mystr = ''

for i in range(10): # сколько чисел должно быть в строке
     mystr += (str(random.randint(0, 100)) + ' ') # интервал, в котором располагаются числа

with open('mynumbers.txt','w') as writenums:
    writenums.write(mystr)

with open('mynumbers.txt','r') as readnums:
    mynums = readnums.readline().strip().split(' ')

print(mynums)

res = sum([float(y) for y in mynums])
print(res)
