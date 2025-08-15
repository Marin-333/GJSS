from numero import NumeroBase

class NumeroBinario(NumeroBase):
    def a_decimal(self) -> int:
        return int(self.valor, 2)

    @classmethod
    def desde_decimal(cls, valor: int):
        return cls(bin(valor)[2:])