"""
Overcomplicated Coffee house example
"""

from abc import abstractmethod, ABC


class Beverage(ABC):

    _desc: str
    _cost: int

    @classmethod
    def get_desc(cls) -> str:
        return cls._desc

    @classmethod
    def cost(cls) -> int:
        return cls._cost


class HouseBlend(Beverage):
    _desc: str = "houseblend"
    _cost: int = 100


class Espresso(Beverage):
    _desc: str = "espresso"
    _cost: int = 150


class DarkRoast(Beverage):
    _desc: str = "dark-roast"
    _cost: int = 200


class AddOn(Beverage):

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_desc(self) -> str:
        return self._beverage.get_desc() + " with " + self._desc

    def cost(self) -> int:
        return self._beverage.cost() + self._cost


class Sugar(AddOn):
    _desc: str = "Sugar"
    _cost: int = 20


class Milk(AddOn):
    _desc: str = "Milk"
    _cost: int = 30


if __name__ == "__main__":
    house_blend = HouseBlend()
    print(f"{house_blend.get_desc()} costs {house_blend.cost()}$")

    milk_addon = Milk(house_blend)
    print(f"{milk_addon.get_desc()} costs {milk_addon.cost()}$")

    sugar_addon = Sugar(milk_addon)
    print(f'{sugar_addon.get_desc()} costs {sugar_addon.cost()}$')

