# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).


class WareHouse:
    def __init__(self, volume, address):
        self.volume = volume
        self.address = address
        # здесь будем хранить объекты поступившего на склад оборудования
        self.contents = []
        # здесь будем хранить место нахождения каждого экземпляра (серийный номер: место хранения)
        self.statuses = {}

    def __add__(self, other):
        # поступление на склад
        # print(other.serial_number)
        if self.statuses.get(other.serial_number) != 'склад':
            self.contents.append(other)
            self.statuses[other.serial_number] = 'склад'
            print(self.statuses)
        else:
            print('Это оборудование уже на складе!')
        return self

    def transmit(self, serial_number, department):
        # передача оборудования в другое подразделение
        if self.statuses.get(serial_number) == 'склад':
            self.statuses[serial_number] = department
            print('Оборудование передано в подазделение', department)
        else:
            print('Такого оборудования на складе нет!')


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
w = WareHouse(2000, 'nowhere')
w += y
w += y
w.transmit(y.serial_number,'IT')
w.transmit(y.serial_number,'IT')

