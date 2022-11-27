from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self) -> Product:
        ...

    def some_operation(self) -> str:
        product = self.factory_method()
        return product.operation()


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        ...


class ConcreteProduct1(Product):

    def operation(self) -> str:
        return "{Result of ConcreteProduct1}"


class ConcreteProduct2(Product):

    def operation(self) -> str:
        return "{Result of ConcreteProduct2}"


def client_code(creator: Creator) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    client_code(ConcreteCreator1())
    print("\n")
    client_code(ConcreteCreator2())
