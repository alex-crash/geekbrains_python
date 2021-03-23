"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag

    def __str__(self):
        real_str = f"({self.__real})" if self.__real < 0 else f"{self.__real}"
        imag_str = f"({self.__imag})*i" if self.__imag < 0 else f"{self.__imag}*i"

        if self.__imag == 0:
            complex_str = real_str
        elif self.__real == 0:
            complex_str = imag_str
        else:
            complex_str = real_str + '+' + imag_str

        return complex_str

    def __add__(self, other):
        real = self.__real + other.__real
        imag = self.__imag + other.__imag

        return Complex(real, imag)

    def __mul__(self, other):
        real = self.__real * other.__real - self.__imag * other.__imag
        imag = self.__real * other.__imag + self.__imag * other.__real

        return Complex(real, imag)


def main():
    a = Complex(1, -4)
    b = Complex(-3, 1)

    print(f"Сложение {a} + {b} = ", end='')
    print(Complex(1, -4) + Complex(-3, 1))

    print(f"Умножение {a} * {b} = ", end='')
    print(Complex(1, -4) * Complex(-3, 1))


if __name__ == '__main__':
    main()
