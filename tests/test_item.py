import pytest
from src.item import Item
from src.InstantiateCSVError import InstantiateCSVError


@pytest.fixture
def item_instance():
    return Item('milk', 59.5, 100)


@pytest.fixture
def item_instance_2():
    return Item('bear', 9.5, 555)


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


def test_add(item_instance, item_instance_2):
    assert item_instance + item_instance_2 == 655
    with pytest.raises(Exception):
        item_instance + 100


def test_exceptions():
    # При удалённом файле items.csv из папки src
    # with pytest.raises(FileNotFoundError):
    #     Item.instantiate_from_csv()

    # При повреждённом файле items.csv
    # with pytest.raises(InstantiateCSVError):
    #     Item.instantiate_from_csv()
