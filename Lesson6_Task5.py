class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Рисование ручкой', self.title)

class Pencil(Stationery):
    def draw(self):
        print('Рисование карандашом', self.title)

class Handle(Stationery):
    def draw(self):
        print('Рисование маркером', self.title)

s0 = Stationery('Bic')
s0.draw()

s1 = Pen('Parker')
s1.draw()

s2 = Pencil('Конструктор')
s2.draw()

s3 = Handle('Made in China')
s3.draw()
