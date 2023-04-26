from pathlib import Path
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    csv_file = Path.joinpath(Path(__file__).parent, 'items.csv')


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name      # private name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property       # name getter


    def name(self):
        return self.__name

    @name.setter     # name setter


    def name(self, name):
        try:
            if len(name) > 10:
                raise ValueError(
                    'Длина наименования товара превышает 10 символов')
            self.__name = name
        except ValueError as exception:
            print(f'Exception: {exception}')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        c_t_p = self.price * self.quantity
        return c_t_p


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @classmethod


    def instantiate_from_csv(cls):
        """
        Класс метод инициализирующий экземпляры класса Item данными
        из файла csv_file.      # путь: src items.csv
        """
        with open(cls.csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'],
                    cls.string_to_number(row['price']),
                    cls.string_to_number(row['quantity']))


    @staticmethod


    def string_to_number(num: str):
        """
        статический метод, возвращающий число из числа строки
        """
        return int(float(num))

