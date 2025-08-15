from tnumeros import Numero

class Binario(Numero):
    def to_decimal(self):
        return int(self._valor, 2)

    def tipo(self):
        return "Binario"
