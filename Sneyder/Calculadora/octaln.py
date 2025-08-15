from tnumeros import Numero

class Octal(Numero):
    def to_decimal(self):
        return int(self._valor, 8)

    def tipo(self):
        return "Octal"
