# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class WareHouse:
    def __init__(self, volume, address):
        self.volume = volume
        self.address = address


class TechInstance:
    def __init__(self, brand, model, tech_length, tech_width, tech_hight):
        self.brand = brand
        self.model = model
        self.tech_length = tech_length
        self.tech_width = tech_width
        self.tech_hight = tech_hight
        self.serial_number = self.__hash__()


class Printer(TechInstance):
    def __init__(self, brand, model, tech_length, tech_width, tech_hight):
        super().__init__(brand, model, tech_length, tech_width, tech_hight)
        self.tech_type = 'Printer'
        self.paper_format = ''
        self.is_color = None


class Scanner(TechInstance):
    def __init__(self, brand, model, tech_length, tech_width, tech_hight):
        super().__init__(brand, model, tech_length, tech_width, tech_hight)
        self.tech_type = 'Scanner'
        self.scan_speed = None
        self.color_depth = None


class Xerox(TechInstance):
    def __init__(self, brand, model, tech_length, tech_width, tech_hight):
        super().__init__(brand, model, tech_length, tech_width, tech_hight)
        self.tech_type = 'Xerox'
        self.copy_speed = None


y = Printer('Hewlett', '456', 400, 300, 250)
print(y.serial_number)
print(y.brand)

x = Scanner('Noname', '123', 400, 300, 250)
print(x.serial_number)
print(x.brand)

z = Xerox('Xerox', '098', 400, 300, 250)
print(z.serial_number)
print(z.brand)
