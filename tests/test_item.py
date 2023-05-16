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
