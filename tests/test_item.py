"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

# for 1 homework
item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 3)
# for 2 hw
item = Item('Телефон', 10000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 60000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 5000
    assert item2.price == 10000


def test_name():
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 8
    item3 = Item.all[0]
    assert item3.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
