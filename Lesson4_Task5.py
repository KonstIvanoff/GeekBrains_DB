from functools import reduce

def proizv(a,b):
    return a*b

print(reduce(proizv,[y for y in range(100, 1000+1) if y % 2 == 0]))


