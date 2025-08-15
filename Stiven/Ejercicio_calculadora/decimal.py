from numero_abstracto import NumeroAbstracto

class Decimal(NumeroAbstracto):

    def __init__(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El valor debe ser un entero decimal")
        super().__init__(valor)
    
    def a_decimal(self) -> int:
        return self.valor
    
    def a_binario(self) -> str:
        if self.valor == 0:
            return "0"
        elif self.valor < 0:
            return "-" + bin(abs(self.valor))[2:]
        else:
            return bin(self.valor)[2:]
    
    def a_octal(self) -> str:
        if self.valor == 0:
            return "0"
        elif self.valor < 0:
            return "-" + oct(abs(self.valor))[2:]
        else:
            return oct(self.valor)[2:]
    
    def a_hexadecimal(self) -> str:
        if self.valor == 0:
            return "0"
        elif self.valor < 0:
            return "-" + hex(abs(self.valor))[2:].upper()
        else:
            return hex(self.valor)[2:].upper()
    
    def a_romano(self) -> str:
        if self.valor == 0:
            return "N"
        elif self.valor < 0:
            return "-" + self._decimal_a_romano(abs(self.valor))
        else:
            return self._decimal_a_romano(self.valor)
    
    def _decimal_a_romano(self, num):
        romanos = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        resultado = ""
        for valor, letra in romanos:
            while num >= valor:
                resultado += letra
                num -= valor
        return resultado
    
    def _crear_instancia_mismo_tipo(self, valor_decimal):
        return Decimal(valor_decimal)
