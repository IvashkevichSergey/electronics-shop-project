import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone_instance():
    return Phone('Samsung 10', 40000, 1000, 2)


def test_repr(phone_instance):
    assert repr(phone_instance) == "Phone('Samsung 10', 40000, 1000, 2)"


def test_getter_number_of_sim(phone_instance):
    assert phone_instance.number_of_sim == 2


def test_setter_number_of_sim(phone_instance):
    phone_instance.number_of_sim = 1
    assert phone_instance.number_of_sim == 1
    with pytest.raises(Exception):
        phone_instance.number_of_sim = 0


def test_add(phone_instance):
    some_item = Item('chair', 2500, 50)
    assert phone_instance + some_item == 1050
    with pytest.raises(Exception):
        phone_instance + 15
