class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__kg_m2_cm = 25
        self.__depth_cm = 5

    def Calc_asph_mass(self):
        return self._length * self._width * self.__kg_m2_cm * self.__depth_cm/1000


r1 = Road(5000, 20)
mt1 = r1.Calc_asph_mass()
print('Требуемая масса - {} тонн.'.format(mt1))

