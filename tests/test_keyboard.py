from src.keyboard import KeyBoard

kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_Mixinlanguage():
    assert str(kb) == "Dark Project KD87A"


assert str(kb.language) == "EN"

kb.change_lang()
assert str(kb.language) == "RU"

# Сделали RU -> EN -> RU
kb.change_lang().change_lang()
assert str(kb.language) == "RU"
