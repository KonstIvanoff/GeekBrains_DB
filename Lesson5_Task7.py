import json

with open('companies.txt','r') as rd:
    mydata = rd.readlines()

def myfunc(x):
    try:
        v = int(x)
        return v
    except ValueError:
        return x

incomes = {}

for i in mydata:
    name, stat, income, cost = map(myfunc, i.split(' '))
    incomes.setdefault(name, income - cost)
    # print(name, stat, income, cost)

print(incomes)

profits = [vl for vl in incomes.values() if vl > 0]
avgprofits = {}
avgprofits.setdefault('average_profit',sum(profits)/len(profits))

print(avgprofits)

with open('jdata.json','w') as jwr:
    json.dump([incomes, avgprofits], jwr)

# [{"firm_1": 5000, "firm_2": -1000, "firm_3": 5000, "firm_4": -3000, "firm_5": 4000, "firm_6": 4000}, {"average_profit": 4500.0}]
