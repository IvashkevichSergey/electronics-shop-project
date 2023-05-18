import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для атрибута name
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Сеттер для атрибута name
        """
        # Вызываем исключение если длина нового имени больше 10 символов
        if len(new_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self._name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Классовый метод, инициализирующий экземпляры класса `Item`
        данными из файла src/items.csv
        """
        # Сохраняем путь до csv файла
        current_directory = os.path.dirname(os.path.dirname(__file__))
        path_to_file = os.path.join(current_directory, 'src', 'items.csv')
        # Открываем csv файл с нужной кодировкой
        with open(path_to_file, encoding='windows-1251') as file:
            reader = csv.DictReader(file).reader
            # Из данных по каждой строке создаём новые экземпляры класса Item,
            # отсекая первую ненужную строку
            for line in reader:
                if reader.line_num == 1:
                    continue
                name, price, quantity = line
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))
