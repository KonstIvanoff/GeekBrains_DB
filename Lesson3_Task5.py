def plus_str(beg_sum, new_str, spec):
    exit_flg = False
    mylist = new_str.split(' ')
    if spec in mylist:
        f = mylist.index(spec)
        mylist = mylist[:f]
        exit_flg = True
    for i in mylist:
        try:
            beg_sum += float(i)
        except ValueError:
            continue
    return beg_sum, exit_flg

end_flg = False
res = 0
spec_symb = 'q'

while not end_flg:
        mystr = input('Введите строку чисел, разделенных пробелами (' + spec_symb + ' - завершение расчета и выход): ')
        res, end_flg = plus_str(res, mystr, spec_symb)
        print('Текущий результат: ', res)

