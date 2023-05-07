from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        """
        Подкласс Phone(Item) содержит все атрибуты класса `Item`
        и дополнительно атрибут - number_of_sim, содержащий количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

    @property  # name getter
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of: int):
        try:
            if 1 <= number_of == int(number_of):
                self.__number_of_sim = number_of
            else:
                raise ValueError
        except ValueError:
            print('Количество физических SIM-карт должно быть целым числом больше нуля.')
