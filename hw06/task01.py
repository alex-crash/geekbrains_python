"""
1. Создать класс TrafficLight (светофор).

определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    COLORS = ["Красный", "Желтый", "Зеленый"]

    TIMINGS = {
        "Красный": 7,
        "Желтый": 2,
        "Зеленый": 7
    }

    def __init__(self):
        self.__color = "Зеленый"

    def running(self):
        tl_cycle = cycle(TrafficLight.COLORS)

        while True:
            next_color = next(tl_cycle)
            next_color_index = TrafficLight.COLORS.index(next_color)
            current_color_index = TrafficLight.COLORS.index(self.__color)
            delay = TrafficLight.TIMINGS[next_color]

            if (current_color_index + 1) % 3 != next_color_index:
                print(f"Некорректный режим: {next_color}!")

            self.__color = next_color
            print(f"{next_color}. Задержка(сек): {delay}")
            sleep(delay)


def main():
    tl = TrafficLight()
    tl.running()


if __name__ == '__main__':
    main()
