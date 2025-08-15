from abc import ABC, abstractmethod

class Numero(ABC):
    def __init__(self, valor):
        self._valor = valor  # Encapsulado

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def to_decimal(self):
        pass

    # Conversiones comunes (reutilizan to_decimal)
    def a_binario(self):
        return bin(self.to_decimal())

    def a_octal(self):
        return oct(self.to_decimal())

    def a_hexadecimal(self):
        return hex(self.to_decimal())

    def a_entero(self):
        return int(self.to_decimal())

    def a_romano(self):
        dec = self.to_decimal()
        if dec <= 0:
            return "No se puede representar en números romanos (debe ser > 0)."
        return self._decimal_a_romano(dec)

    def _decimal_a_romano(self, num):
        valores = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        resultado = ""
        for arabigo, romano in valores:
            while num >= arabigo:
                resultado += romano
                num -= arabigo
        return resultado
