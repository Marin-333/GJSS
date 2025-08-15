from numero import NumeroBase

class NumeroDecimal(NumeroBase):
    def a_decimal(self) -> int:
        return int(self.valor)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(str(valor))