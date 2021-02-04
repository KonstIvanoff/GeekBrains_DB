# заполняем массив
mylist = []

while(True):
    answ = input('Введите следующее значение списка (q для окончания): ')
    if answ == 'q':
        break
    else:
        mylist.append(answ)

print(mylist)

for i in range(1,len(mylist),2):

    # current = mylist[i]
    # mylist[i] = mylist[i-1]
    # mylist[i - 1] = current

    mylist[i],mylist[i - 1] = mylist[i - 1],mylist[i]

print (mylist)