# my_list = [7, 5, 3, 3, 2]
# my_list = sorted(my_list,  reverse = True)
my_list = []
while(True):
    i = (input('Введите новое значение для рейтинга (q-выход): '))
    if i == 'q':
        break
    else:
        try:
            y = int(i)
        except ValueError:
            print('Ошибка!')
            continue
        my_list.append(y)
        my_list.sort(reverse=True)
        print(my_list)