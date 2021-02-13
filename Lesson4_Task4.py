mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = [y for y in mylist if mylist.count(y) == 1]
print(res)