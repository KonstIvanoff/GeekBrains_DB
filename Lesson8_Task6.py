# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

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

        # валидация - должен быть объект нужного класса
        if not isinstance(other, TechInstance):
            print('Хранение этого товара на складе оргтехники невозможно.')
            return self

        if self.statuses.get(other.serial_number) != 'склад':
            self.contents.append(other)
            self.statuses[other.serial_number] = 'склад'
            print('Оборудование', other, 'принято на склад.')
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
        # валидация
        if str(tech_length).isdigit() or not str(tech_width).isdigit() or not str(tech_hight).isdigit():
            print('Габариты прибора заданы некорректно!')
        else:
            self.tech_length = tech_length
            self.tech_width = tech_width
            self.tech_hight = tech_hight
        self.serial_number = self.__hash__()

    def __str__(self):
        return self.brand + ' ' + self.model + ' ' + str(self.serial_number)


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

w += w

z = Scanner('Canon', '2020', 'jfwekj', 200, 70)
w += z

