from tnumeros import Numero

class Hexadecimal(Numero):
    def to_decimal(self):
        return int(self._valor, 16)

    def tipo(self):
        return "Hexadecimal"
