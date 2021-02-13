from itertools import count, cycle

bound = 10

for i in count(1):
    if i > bound:
        break
    print(i)

cc = ['morning','afternoon','evening','night']
j = 0
bound = 7

for i in enumerate(cycle(cc)):
    print(i)
    j+=1
    if j > 7*4: # week
        break






