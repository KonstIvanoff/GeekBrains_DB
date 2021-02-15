sav = []
while True:
    myline = input('Введите, что нужно написать в строку файла (ввод для завершения): ')
    if myline == '':
        break
    myline += '\n'
    sav.append(myline)
# print(sav)

with open('myfile.txt','w') as writer:
    writer.writelines(sav)


