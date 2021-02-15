mydict= {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

engfile = open('eng_numbers.txt','r')
rufile = open('ru_numbers.txt','w',encoding = 'utf-8')

for myrow in engfile:
    engword = myrow.split(' ')[0]
    myrow = myrow.replace(engword, mydict.get(engword))
    rufile.write(myrow)

engfile.close()
rufile.close()




