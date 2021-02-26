import random

class LotoNumbers:
    def __init__(self, quant):
        self.maxnum = 90
        self.quant = quant
        self.counter = 0
        self.numbers = []
        self.get_numbers()
        # print(self.numbers)

    def get_numbers(self):
        for i in range(1,self.maxnum+1):
            self.numbers.append(i)

    def __next__(self):
        # print('Длина массива', len(self.numbers))
        if len(self.numbers) == 0 or self.counter == self.quant:
            raise StopIteration
        else:
            num = random.randint(0, len(self.numbers)) - 1
            res = self.numbers.pop(num)
            self.counter += 1
            return res

class IterLotoNumbers:
    def __init__(self, quant = 90):
        # сколько чисел из 90 вернуть
        self.quant = quant

    def __iter__(self):
        return LotoNumbers(self.quant)

class LotoCard:
    def __init__(self, name = 'Noname'):
        self.name = name
        self.numbers = []
        self.rows = 3
        self.columns = 5
        self.numbers_count = self.rows * self.columns
        self.crossed = 0
        self.fill()

    def fill(self):
        # получаем числа для карточки
        nums = IterLotoNumbers(self.numbers_count)
        buf = []
        for j, i in enumerate(nums, start=1):
            buf.append(i)
            # print(j, i)

        # формируем ряды карточки
        for i in range(self.rows):
            myrow = sorted(buf[i*self.columns: (i+1)*self.columns])
            pos_spaces = list(range(self.columns))

            # вставка пробелов
            for i in range(self.columns):
                pos = random.randint(0, len(myrow))
                myrow.insert(pos, ' ')

            # print(myrow)
            self.numbers.append(myrow)

    def __str__(self):
        res = self.name + '\n'
        res += ('___'*2*self.columns) + '\n'
        for r in self.numbers:
            for c in r:
                res += '{:>2} '.format(str(c))
            res += '\n'
        res += ('---' * 2 * self.columns) + '\n'
        return res

    def cross_out(self, number):
        found = False
        for r in self.numbers:
            i = self.numbers.index(r)
            for c in r:
                j = list(r).index(c)
                if str(c).isdigit():
                    if number == int(c):
                        self.numbers[i][j] = '--'
                        self.crossed += 1
                        found = True
        crossoutall = (True if self.crossed == self.numbers_count else False)
        return found, crossoutall

class LotoGame():
    def __init__(self):
        pass

    def start_game(self):
        c0 = LotoCard("Карта компа")
        c1 = LotoCard("Карта игрока")
        kegs = IterLotoNumbers()
        for n, i in enumerate(kegs, start=1):
            print(c0, c1, end='')
            print('Ход {}.'.format(n))
            print('Выбран бочонок с числом {:>2} !'.format(i))
            f0, r0 = c0.cross_out(i)
            f1, r1 = c1.cross_out(i)
            answ = input('Зачеркнуть ? y/n: ')
            if answ == 'y':
                if not f1:
                    print('Ты проиграл! Такого числа нет в карте!')
                    return
            elif answ != 'y' and f1:
                print('Ты проиграл! Это число было в карте!')
                return

            if r0 and r1:
                print('Боевая ничья! Числа зачеркнуты в обеих картах!')
                return
            elif r0:
                print('Победа компьютера! Он зачеркнул все числа в карте!')
                return
            elif r1:
                print('Ты выиграл! Зачеркнуты все числа в карте!')
                return

game = LotoGame()
game.start_game()


