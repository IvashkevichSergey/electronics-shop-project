from src.item import Item


class Phone(Item):
    """
    Класс для представления товара Phone в магазине.
    """
    def __init__(self, name: str, price: int,
                 quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых телефоном сим-карт
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        """
        Отображение информации об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, " \
               f"{self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер для атрибута number_of_sim
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """
        Сеттер для атрибута number_of_sim
        """
        # Вызываем исключение если количество сим-карт меньше 1
        if num <= 0:
            raise ValueError('Количество физических SIM-карт должно быть '
                             'целым числом больше нуля')
        else:
            self._number_of_sim = num
