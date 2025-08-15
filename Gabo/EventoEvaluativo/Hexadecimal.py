from numero import NumeroBase

class NumeroHexadecimal(NumeroBase):
    def a_decimal(self) -> int:
        return int(self.valor, 16)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(hex(valor)[2:])