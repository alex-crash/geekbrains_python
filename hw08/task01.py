"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
import re

DAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class DateParseException(Exception):
    pass


class DateSplitException(DateParseException):
    pass


class GeneralDateValidationException(DateSplitException):
    pass


class MonthValidationException(GeneralDateValidationException):
    pass


class DayValidationException(GeneralDateValidationException):
    pass


class Date:
    def __init__(self, date_string: str):
        regex = re.compile('^([0-9]{2}-){2}[0-9]{4}$')
        if regex.match(date_string) is not None:
            self.date_string = date_string
        else:
            print("Неправильный формат даты")
            raise DateParseException

    @classmethod
    def split(cls, date_string: str):
        try:
            date_list = list(map(int, cls(date_string).date_string.split('-')))
        except (DateParseException, ValueError):
            print("Не удалось получить список компонентов даты")
            raise DateSplitException
        else:
            return date_list

    @staticmethod
    def validate(date_string: str):
        try:
            day, month, year = Date.split(date_string)
        except GeneralDateValidationException:
            print("Валидация даты не прошла успешно")
        else:
            if not 1 <= month <= 12:
                print("Валидация месяца не прошла успешно")
                raise MonthValidationException
            if not 1 <= day <= DAYS[month]:
                print("Валидация числа не прошла успешно")
                raise DayValidationException

            return True


def main():
    print(".: Тест 1 :.")
    try:
        Date("03-02-19384")
    except DateParseException:
        print("Совсем неправильный формат даты")

    print(".: Тест 2 :.")
    print(f"Дата: {Date('03-02-1934').date_string}")

    print(".: Тест 3 :.")
    try:
        Date.split("403-02-1938")
    except DateSplitException:
        print("Не совсем, но, все-таки, неправильный формат даты. Возможно, в дату закралось не число?")

    print(".: Тест 4 :.")
    print(f"Список компонентов даты: {Date.split('03-02-1938')}")

    print(".: Тест 5 :.")
    try:
        Date.validate('03-00-1938')
    except MonthValidationException:
        print("Что-то случилось с месяцем в дате")

    print(".: Тест 6 :.")
    try:
        Date.validate('31-04-1938')
    except DayValidationException:
        print("Что-то случилось с днем месяца")

    print(".: Тест 7 :.")
    print(f"Дата валидируется успешно: {Date.validate('03-02-1938')}")


if __name__ == '__main__':
    main()
