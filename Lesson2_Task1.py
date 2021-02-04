mylist = [1, 1.2, 'preved', [1,2,3],(4,5,6,7),{'a','b','b','c'}, {'1':'первый', '2':'второй'}, ZeroDivisionError]

for i in mylist:
    print(i, end = ' ')
    print(type(i))