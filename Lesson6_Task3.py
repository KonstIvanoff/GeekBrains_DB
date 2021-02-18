class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def getfullname(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        i = sum([x for x in self._income.values()])
        return i

inc = {'salary':20000, 'bonus':10000, 'revenue':50000, 'rent':25000}
pers = Position('Вася','Пупкин','Дворник',inc)

print(pers.name, pers.surname, pers.position)
print('Полное имя {}.'.format(pers.getfullname()) )
print('Суммарный доход {}.'.format(pers.get_total_income()))

