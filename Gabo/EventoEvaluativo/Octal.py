from numero import NumeroBase

class NumeroOctal(NumeroBase):
    def a_decimal(self) -> int:
        return int(self.valor, 8)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(oct(valor)[2:])