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
        super().__init__()
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

    def __add__(self, other):
        """
        Сложение экземпляров классов Phone и Item
        по количеству товара в магазине
        """
        if not isinstance(other, Item):
            raise ValueError('Допустимо сложение только '
                             'экземпляров классов Phone и Item')
        else:
            return self.quantity + other.quantity

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

    def __repr__(self):
        """
        Отображение информации об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity})"

    def __str__(self):
        """
        Отображение информации об объекте класса для пользователей
        """
        return self.name

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
            cls.all.clear()
            reader = csv.DictReader(file)
            # Из данных по каждой строке создаём
            # новые экземпляры класса Item
            for line in reader:
                name, price, quantity = \
                    line['name'], line['price'], line['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(string))
