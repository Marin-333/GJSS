from tnumeros import Numero

class Romano(Numero):
    def to_decimal(self):
        return self._romano_a_decimal(self._valor.upper())

    def tipo(self):
        return "Romano"

    def _romano_a_decimal(self, roman):
        valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        prev = 0
        for letra in reversed(roman):
            val = valores.get(letra, 0)
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
