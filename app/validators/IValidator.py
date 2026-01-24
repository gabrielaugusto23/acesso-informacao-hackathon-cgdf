from abc import ABC, abstractmethod


class IValidator(ABC):
    def __init__(self, next_handler=None):
        self.__next_handler = next_handler

    def set_next(self, handler):
        self.__next_handler = handler
        return handler

    @abstractmethod
    def handle(self, text: str):
        pass
