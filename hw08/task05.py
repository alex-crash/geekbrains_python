"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

from task04 import OfficeEquipmentStore, StoreCapacityException, Printer, Scanner, Xerox


class EnhancedOfficeEquipmentStore(OfficeEquipmentStore):
    def receive(self, goods: list):
        try:
            self.store(goods)
        except StoreCapacityException as e:
            print(f"Невозможно получить товар")
            raise(StoreCapacityException(e.message))

    def send(self, amount: int):
        try:
            goods = self.discard(amount)
        except StoreCapacityException as e:
            print(f"Невозможно отправить товар")
            raise (StoreCapacityException(e.message))
        else:
            return goods


def main():
    print(".: Тест 1 :.")
    store = EnhancedOfficeEquipmentStore(3)
    store.receive([Printer('600x600', True), Scanner("1200x1200", 400), Xerox("300x300", False)])
    print("Оборудование получено успешно")

    print(".: Тест 2 :.")
    try:
        store.receive([Printer('600x600', True)])
    except StoreCapacityException as e:
        print(e)

    print(".: Тест 3 :.")
    try:
        store.send(4)
    except StoreCapacityException as e:
        print(e)

    print(".: Тест 4 :.")
    store.send(3)
    print(f"Оборудование отправлено")


if __name__ == '__main__':
    main()
