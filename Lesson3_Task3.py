def my_func(a1, a2, a3):
    mylist = [a1,a2,a3]
    mylist.sort(reverse=True)
    res = sum(mylist[:2])
    return res


print(my_func(14,9,18))