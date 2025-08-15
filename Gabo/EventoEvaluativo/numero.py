from abc import ABC, abstractmethod

class NumeroBase(ABC):
    def __init__(self, valor: str):
        self.valor = valor

    @abstractmethod
    def a_decimal(self) -> int:
        pass

    @classmethod
    @abstractmethod
    def desde_decimal(cls, valor: int):
        pass

    def __add__(self, otro):
        return self.__class__.desde_decimal(self.a_decimal() + otro.a_decimal())

    def __sub__(self, otro):
        return self.__class__.desde_decimal(self.a_decimal() - otro.a_decimal())

    def __mul__(self, otro):
        return self.__class__.desde_decimal(self.a_decimal() * otro.a_decimal())

    def __truediv__(self, otro):
        return self.__class__.desde_decimal(self.a_decimal() // otro.a_decimal())

    def __str__(self):
        return f"{self.__class__.__name__}({self.valor})"
