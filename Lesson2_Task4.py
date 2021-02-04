mysent = input('Введите предложение: ')
mywords = mysent.split(' ')

# print(mywords)

j = 0
for i in mywords:
    y = i.replace(' ','')
    if y == '':
        continue
    else:
        j = j + 1
        print('{}. {}'.format(j,i))

