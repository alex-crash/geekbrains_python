"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def name(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def consumption(self):
        return 2 * self.height + 0.3


def main():
    print(f"Расход ткани для пальто 64 размера: {Coat('Пальто для коня', 64).consumption}")
    print(f"Расход ткани для костюма ростом 2 м: {Suit('Костюм для двухметровой оглобли', 2).consumption}")


if __name__ == '__main__':
    main()
