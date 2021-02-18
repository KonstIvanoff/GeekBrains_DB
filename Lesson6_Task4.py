class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print('Текущая скорость {} км/ч.'.format(self.speed))

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Остановились!')

    def turn(self,  direction):
        if direction in ('left','to left','налево'):
            print('Повернули налево!')
        elif direction in ('right','to right','направо'):
            print('Повернули направо!')
        else:
            print('Развернулись!')

class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость {} км/ч.'.format(self.speed))
        if self.speed > 60:
            print('Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость {} км/ч.'.format(self.speed))
        if self.speed > 40:
            print('Превышение скорости!')

class PoliceCar(Car):
    pass


mycar = Car(speed=50,color='прозрачный',name='ока',is_police=False)
print(mycar.name, mycar.is_police,mycar.color,mycar.speed)
mycar.go()
mycar.show_speed()
mycar.turn('налево')
mycar.turn('направо')
mycar.turn('куданибудь')
mycar.stop()

print()

othercar = TownCar(speed=90,color='белый',name='лада',is_police=False)
othercar.go()
othercar.show_speed()
othercar.turn('налево')
othercar.turn('направо')
othercar.turn('куданибудь')
othercar.stop()

print()

bigcar = WorkCar(speed=60,color='ржавый',name='камаз',is_police=False)
bigcar.show_speed()