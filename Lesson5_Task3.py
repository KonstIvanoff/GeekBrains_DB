with open('employees.txt','r') as r1:
    mydata = r1.readlines()

# print(mydata)

def preobr(s0):
    pre = s0.strip().split(' ')
    pre[1] = float(pre[1])
    return pre

p1 = [preobr(s)[0] for s in mydata if preobr(s)[1] < 20000]
print(p1)
# ['Баранов', 'Васильев']

p2 = sum([float(preobr(s)[1]) for s in mydata])/len(mydata)
print(p2)
# 24000.0


# Афанасьев 25000
# Баранов 15000
# Васильев 18000
# Гарин 30000
# Дорофеев 35000
# Жаров 21000
# Зверев 2400