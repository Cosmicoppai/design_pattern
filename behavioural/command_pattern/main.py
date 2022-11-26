"""
The main pattern is to inculcate a higher degree
of loose coupling between involved parties
"""
from __future__ import annotations

"""
Command is a behavioral design pattern that converts requests or
simple operation into objects
"""

"""
Usage Example:
The command pattern is pretty common.
Most often it’s used as an alternative for callbacks to parameterizing UI elements with actions.
 It’s also used for queueing tasks, tracking operations history, etc
"""

"""
Identification:
The Command pattern is recognizable by behavioral methods in an abstract/interface type (sender)
 which invokes a method in an implementation of a different abstract/interface type (receiver)
  which has been encapsulated by the command implementation during its creation.
Command classes are usually limited to specific actions.
"""

from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        ...


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(self._payload)


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._receiver.do_something(self._a)
        self._receiver.do_something(self._b)


class Receiver:
    def do_something(self, a: str) -> None:
        print(a)

    def do_something_else(self, b: str) -> None:
        print(b)


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send Mail", "Save Report"))

    invoker.do_something_important()
