def calc_hours(arr):
    vl = 0
    for i in arr:
        num = ''
        for c in i:
            if c.isdigit():
                num += c
        vl += (float(num) if not num == '' else 0)
    return int(vl)

with open('learning.txt','r') as wr:
    lrn = wr.readlines()

res = {}

for row in lrn:
    s0 = row.split()
    k0 = s0.pop(0).replace(':','')
    v0 = calc_hours(s0)
    res.setdefault(k0,v0)

print(res)
