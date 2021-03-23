"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod


class StoreCapacityException(Exception):
    def __init__(self, message: str):
        self.message = message


class ResolutionParseException(Exception):
    def __init__(self, message: str):
        self.message = message


class OfficeEquipmentStore:
    def __init__(self, capacity: int):
        self.__storage = []
        self.__capacity = capacity

    def store(self, equipment: list):
        amount = len(equipment)
        if amount > self.__capacity:
            raise StoreCapacityException(f"Количество оборудования превышает оставшуюся вместимость склада, "
                                         f"вместимость: {self.__capacity}, товаров: {amount}")
        else:
            self.__capacity -= amount
            self.__storage.extend(equipment)

    def discard(self, amount: int):
        store_amount = len(self.__storage)
        if amount > store_amount:
            raise StoreCapacityException(f"Количество оборудования превышает имеющееся в наличии, "
                                         f"в наличии {store_amount}, запрошено: {amount}")
        else:
            equipment = self.__storage[:amount]
            self.__capacity += amount
            self.__storage = self.__storage[amount:]

            return equipment


class Equipment(ABC):
    @property
    @abstractmethod
    def resolution(self):
        pass


class OfficeEquipment(Equipment):
    def __init__(self, resolution: str):
        self.resolution = resolution

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str):
        if len(resolution.split('x')) < 2:
            raise ResolutionParseException("Разрешение должно иметь 2 измерения")
        else:
            self.__resolution = resolution


class Printer(OfficeEquipment):
    def __init__(self, resolution: str, color: bool):
        super().__init__(resolution)
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: bool):
        self.__color = color


class Scanner(OfficeEquipment):
    def __init__(self, resolution: str, speed: int):
        super().__init__(resolution)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed


class Xerox(OfficeEquipment):
    def __init__(self, resolution: str, fax: bool):
        super().__init__(resolution)
        self.fax = fax

    @property
    def fax(self):
        return self.__fax

    @fax.setter
    def fax(self, fax: bool):
        self.__fax = fax


def main():
    print(".: Тест 1 :.")
    try:
        OfficeEquipmentStore(2).store([Printer('600x600', True), Scanner("1200x1200", 400), Xerox("300x300", False)])
    except StoreCapacityException as e:
        print(e)

    print(".: Тест 2 :.")
    try:
        OfficeEquipmentStore(3).store([Printer('600x600', True), Scanner("12001200", 400), Xerox("300x300", False)])
    except ResolutionParseException as e:
        print(e)

    print(".: Тест 3 :.")
    store = OfficeEquipmentStore(3)
    store.store([Printer('600x600', True), Scanner("1200x1200", 400), Xerox("300x300", False)])
    print("Товары получены успешно")

    print(".: Тест 4 :.")
    try:
        store.discard(4)
    except StoreCapacityException as e:
        print(e)

    print(".: Тест 5 :.")
    store.discard(1)
    print(f"Товары отправлены успешно")

    print(".: Тест 6 :.")
    try:
        store.store([Printer('600x600', True), Xerox("300x300", False)])
    except StoreCapacityException as e:
        print(e)

    print(".: Тест 7 :.")
    store.store([Printer('600x600', True)])
    print("Товары получены успешно")


if __name__ == '__main__':
    main()
