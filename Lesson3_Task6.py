def int_func(word):
    return(word.title())

def proc_sent(sent):
    mylist = sent.split(' ')
    res = ''
    for i in mylist:
        i = int_func(i)
        res += (i + ' ')
    return res.rstrip()

str1 = 'я счастливей всех на свете'
print(proc_sent(str1))

