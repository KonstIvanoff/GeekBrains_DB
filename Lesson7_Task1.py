class Matrix:
    def __init__(self, mtr):
        self.Mtr = mtr
        self._columns = len(mtr)
        self._rows = len(mtr[0])

    def __str__(self):
        res = ''
        for i in self.Mtr:
            for j in i:
                res += str(j) + ' '
            res += '\n'
        return res

    def __add__(self, other):
        if self._columns != other._columns or self._rows != other._rows:
            raise ValueError
        else:
            res = []
            for i in range(self._columns):
                r0 = []
                for j in range(self._rows):
                    r0.append(self.Mtr[i][j] + other.Mtr[i][j])
                res.append(r0)
            return Matrix(res)

m = [[7,8,9],[3,2,1],[4,5,6]]
y = Matrix(m)
print(y)
# print(y._columns, y._rows)

k = [[11,1,6],[22,13,10],[14,25,4]]
x = Matrix(k)
print(x)

z = y + x
print(z)



