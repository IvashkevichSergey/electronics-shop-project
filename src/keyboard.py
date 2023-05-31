from src.item import Item


class ChangeLang:
    """
    Класс для хранения и для изменения раскладки клавиатуры.
    При инициализации язык раскладки - EN
    """
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        """
        Метод изменяет раскладку клавиатуры на противоположную
        """
        self._language = 'RU' if self._language == 'EN' else 'EN'
        return self


class Keyboard(Item, ChangeLang):
    """
    Класс для представления товара Keyboard в магазине.
    """
    @property
    def language(self):
        """
        Метод для получения текущей раскладки клавиатуры
        """
        return self._language
