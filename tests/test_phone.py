from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_repr():
    assert Phone.__repr__(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    assert Phone.__str__(phone1) == 'iPhone 14'


def test___add__():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_number_of_sim_setter():
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
