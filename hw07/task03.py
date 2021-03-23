"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (
__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
"""


class IsNotCellException(Exception):
    def __init__(self, message):
        self.message = message


class IllegalOperationException(Exception):
    def __init__(self, message):
        self.message = message


class Cell:
    @property
    def nucleus(self):
        return self.__nucleus

    @nucleus.setter
    def nucleus(self, nucleus: int):
        self.__nucleus = nucleus

    def __init__(self, nucleus: int):
        self.nucleus = nucleus

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.nucleus + other.nucleus)
        else:
            raise IsNotCellException("В операции должны участвовать две клетки")

    def __sub__(self, other):
        if isinstance(other, Cell):
            if self.nucleus > other.nucleus:
                return Cell(self.nucleus - other.nucleus)
            else:
                raise IllegalOperationException("Разность количества ячеек двух клеток должна быть больше нуля")
        else:
            raise IsNotCellException("В операции должны участвовать две клетки")

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.nucleus * other.nucleus)
        else:
            raise IsNotCellException("В операции должны участвовать две клетки")

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.nucleus // other.nucleus)
        else:
            raise IsNotCellException("В операции должны участвовать две клетки")

    def make_order(self, amount: int):
        rows = self.nucleus // amount
        remainder = self.nucleus % amount
        return ('*' * amount + '\n') * rows + ('*' * remainder)


def main():
    print("Ячейка 1: ")
    print((Cell(3) * Cell(4)).make_order(5))

    print("Ячейка 2: ")
    print((Cell(25) - Cell(10)).make_order(5))

    print("Ячейка 3: ")
    try:
        print((Cell(10) - Cell(11)).make_order(5))
    except IllegalOperationException as e:
        print(e)


if __name__ == '__main__':
    main()
