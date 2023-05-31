from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard_instance():
    return Keyboard('Logitech G G13', 2500, 95)


def test_get_keyboard_info(keyboard_instance):
    assert keyboard_instance.language == 'EN'
    assert keyboard_instance.name == 'Logitech G G13'
    assert keyboard_instance.price == 2500


def test_change_language(keyboard_instance):
    keyboard_instance.change_lang()
    assert keyboard_instance.language == 'RU'
    keyboard_instance.change_lang()
    assert keyboard_instance.language == 'EN'
    keyboard_instance.change_lang().change_lang()
    assert keyboard_instance.language == 'EN'


def test_set_language(keyboard_instance):
    with pytest.raises(Exception):
        keyboard_instance.language = 'RU'
