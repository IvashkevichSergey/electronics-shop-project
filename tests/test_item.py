import pytest
from src.item import Item


@pytest.fixture
def item_instance():
    return Item('milk', 59.5, 100)


def test_item_params(item_instance):
    assert item_instance.price == 59.5
    assert item_instance.quantity == 100


def test_calculate_price(item_instance):
    assert item_instance.calculate_total_price() == 5950


def test_apply_discount(item_instance):
    item_instance.apply_discount()
    assert item_instance.price == 59.5
    Item.pay_rate = 0.5
    item_instance.apply_discount()
    assert item_instance.price == 59.5 * 0.5


def test_name(item_instance):
    assert item_instance.name == 'milk'
    with pytest.raises(Exception):
        item_instance.name = 'blablablabla'


def test_name_setter(item_instance):
    item_instance.name = 'beer'
    assert item_instance.name == 'beer'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[-1].name == 'Клавиатура'


def test_string_to_number():
    assert Item.string_to_number('15.8') == 15
    assert Item.string_to_number('0.1') == 0


def test_repr(item_instance):
    assert repr(item_instance) == "Item('milk', 59.5, 100)"


def test_str(item_instance):
    assert str(item_instance) == 'milk'
