"""
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула ${direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def print_car_info(self):
        print(f"Скорость: {self.speed}, цвет: {self.color}, название: {self.name}, полиция: {self.is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def main():
    tc = TownCar(61, "зеленый", "Town Car")
    sc = SportCar(190, "красный", "Sport Car")
    wc = WorkCar(41, "белый", "Work Car")
    pc = PoliceCar(120, "синий", "Police Car")

    cars = (tc, sc, wc, pc)
    [(car.print_car_info(), car.show_speed()) for car in cars]


if __name__ == '__main__':
    main()
