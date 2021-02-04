# заполняем list
myseasons = ['']
for i in range(1,13):
    if i < 3:
        myseasons.append('зима')
    elif i < 6:
        myseasons.append('весна')
    elif i < 9:
        myseasons.append('лето')
    elif i < 12:
        myseasons.append('осень')
    else:
        myseasons.append('зима')

# print(myseasons)

# заполняем dict
myseasonsd = {}
for i in range(1,13):
    if i < 3:
        myseasonsd[i] = 'зима'
    elif i < 6:
        myseasonsd[i] = 'весна'
    elif i < 9:
        myseasonsd[i] = 'лето'
    elif i < 12:
        myseasonsd[i] = 'осень'
    else:
        myseasonsd[i] = 'зима'

# print(myseasonsd)


try:
    # запрос месяца
    mnth = int(input('Введите номер месяца: '))
except ValueError:
    print('Введен не номер.')
else:
    # результат
    if mnth in range(1,13):
        print('Время года из list: {}'.format(myseasons[mnth]))
        print('Время года из dict: {}'.format(myseasonsd[mnth]))
    else:
        print('Введен неверный номер.')