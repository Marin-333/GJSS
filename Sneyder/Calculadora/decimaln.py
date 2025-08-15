from tnumeros import Numero

class Decimal(Numero):
    def to_decimal(self):
        return int(self._valor)

    def tipo(self):
        return "Decimal"
