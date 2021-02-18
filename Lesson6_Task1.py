import itertools as iter, time

class TrafficLight():
    # lights = {'Красный':7,':Желтый':2,'Зеленый':5}
    def __init__(self):
        self.__color = ''
        self.__lights = {'Красный':7,'Желтый':2,'Зеленый':5}


    def running(self):
        for i, j in iter.cycle(self.__lights.items()):
            print(i)
            time.sleep(j)

s = TrafficLight()
s.running()




