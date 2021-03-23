"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""

from task04 import OfficeEquipment, Printer, Scanner, Xerox
from task05 import EnhancedOfficeEquipmentStore


class IllegalArgumentException(Exception):
    def __init__(self, message):
        self.message = message


class SuperOfficeEquipmentStore(EnhancedOfficeEquipmentStore):
    def __init__(self, capacity: int):
        if not isinstance(capacity, int):
            raise IllegalArgumentException("Вместимость хранилища должна быть целым числом")
        else:
            super().__init__(capacity)

    def receive(self, goods: list):
        if not isinstance(goods, list):
            raise IllegalArgumentException("Ожидается список товаров")
        else:
            super().receive(goods)

    def send(self, amount: int):
        if not isinstance(amount, int):
            raise IllegalArgumentException("Количество товаров должно быть целым числом")
        else:
            super().send(amount)


class SuperOfficeEquipment(OfficeEquipment):
    def __init__(self, resolution: str):
        if not isinstance(resolution, str):
            raise IllegalArgumentException("Разрешение должно быть строкой: два измерения, разделенные знаком x")
        else:
            super().__init__(resolution)


class SuperPrinter(Printer, SuperOfficeEquipment):
    def __init__(self, resolution: str, color: bool):
        if not isinstance(color, bool):
            raise IllegalArgumentException("Принтер либо цветной, либо нет, ожидается параметр логического типа")
        SuperOfficeEquipment.__init__(self, resolution)
        Printer.__init__(self, resolution, color)


class SuperScanner(Scanner, SuperOfficeEquipment):
    def __init__(self, resolution: str, speed: int):
        if not isinstance(speed, int):
            raise IllegalArgumentException("Скорость работы сканера должна быть целым числом")
        SuperOfficeEquipment.__init__(self, resolution)
        Scanner.__init__(self, resolution, speed)


class SuperXerox(Xerox, SuperOfficeEquipment):
    def __init__(self, resolution: str, fax: bool):
        if not isinstance(fax, bool):
            raise IllegalArgumentException("Наличие или отсутствие факса определяется логическим типом")
        SuperOfficeEquipment.__init__(self, resolution)
        Xerox.__init__(self, resolution, fax)


def main():
    print(".: Тест 1 :.")
    try:
        SuperOfficeEquipmentStore("test")
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 2 :.")
    store = SuperOfficeEquipmentStore(3)
    print("Склад создан")

    print(".: Тест 3 :.")
    try:
        store.receive(True)
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 4 :.")
    store.receive([SuperPrinter('600x600', True), SuperScanner("1200x1200", 400), SuperXerox("300x300", False)])
    print("Товары получены")

    print(".: Тест 5 :.")
    try:
        store.send("test")
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 6 :.")
    store.send(1)
    print("Товары отправлены")

    print(".: Тест 7 :.")
    try:
        SuperPrinter(True, True)
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 8 :.")
    try:
        SuperPrinter('600x600', 1)
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 9 :.")
    try:
        SuperScanner("1200x1200", "bla")
    except IllegalArgumentException as e:
        print(e)

    print(".: Тест 10 :.")
    try:
        SuperXerox("300x300", "test")
    except IllegalArgumentException as e:
        print(e)


if __name__ == '__main__':
    main()
