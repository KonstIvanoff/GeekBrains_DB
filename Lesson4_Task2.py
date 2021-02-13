
pre = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res = [y for j, y in enumerate(pre) if y > pre[j-1] and not j == 0]
print(res)


