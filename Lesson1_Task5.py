# запрос выручки компании
income = float(input('Введите выручку компании, млн.руб. : '))
# запрос издержек компании
cost = float(input('Введите издержки компании, млн.руб. : '))
# прибыль компании
profit = (income - cost)
# print('Прибыль: {}'.format(profit))

# рентабельность выручки
rent_income = 0
# количество сотрудников
empl_quant = 0
# прибыль на 1 сотрудника
profit_per_empl = 0

if profit > 0:
    rent_income = 100 * (profit / income)
    print('Фирма работает с прибылью.')
    print('Рентабельность выручки составляет {:.1f} %'.format(rent_income))
    empl_quant = int(input('Введите количество сотрудников: '))
    profit_per_empl = (profit / empl_quant)
    print('Прибыль на одного сотрудника составляет {:.2f} млн.руб.'.format(profit_per_empl))
else:
    print('Фирма работает с убытком.')

