from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc_cloth(self):
        pass

class Coat(Clothes):
    @property
    def calc_cloth(self):
        return (self.size/6.5) + 0.5

class Suit(Clothes):
    @property
    def calc_cloth(self):
        return (2 * self.size) + 0.3

ss = []
ss.append(Coat(2))
ss.append(Coat(1.5))
ss.append(Suit(2.5))
ss.append(Suit(1))

res = sum(i.calc_cloth for i in ss)
print (res)
