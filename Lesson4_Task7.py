import math, itertools

def fact():
    for i in itertools.count(1):
        yield math.factorial(i)

for j, i in enumerate(fact(), start=1):
    print(j, i)
    if j > 10:
        break



