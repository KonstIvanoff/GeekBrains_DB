
# СБОР ДАННЫХ
# названия полей
mytitles = ['название','цена','количество','ед']
# счетчик товаров
j = 0
# результат (список)
res = []
# запись (кортеж)
row = ()
# данные о товаре (словарь)
goods = {}

while(True):
    j = j + 1
    print('Товар {}.'.format(j))
    goods = {}
    for i in mytitles:
        answ = input('Введите ' + str(i) + ': ')
        goods[i] = answ
    # print(goods)
    row = (j, goods)
    # print(row)
    res.append(row)
    cont = input('Ввести следующий товар? y/n д/н: ')
    if cont in ('y','д'):
        continue
    else:
        break

# вывод структуры
print('ЭТО СТРУКТУРА')
# print(res)
for k in res:
    print(k)

# СБОР АНАЛИТИКИ
analytcs = {}
myvalues = []

# значения из словарей
for i in res:
    for k in i[1].values():
        myvalues.append(k)
# print(myvalues)

# заголовок
titles_dict = res[0][1].keys()

# формируем словарь результата
j = 0
for k in titles_dict:
    vlist = []
    for i in range(j,len(myvalues),4):
        vlist.append(myvalues[i])
    analytcs[k] = vlist
    j = j + 1
    #print(vlist)

print('ЭТО АНАЛИТИКА')
print(analytcs)
