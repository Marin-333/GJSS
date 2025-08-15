from numero_abstracto import NumeroAbstracto

class Hexadecimal(NumeroAbstracto):

    def __init__(self, valor):
        if isinstance(valor, str):

            if not all(digito in '0123456789ABCDEFabcdef' for digito in valor):
                raise ValueError("El valor debe ser una cadena hexadecimal válida (0-9, A-F)")
            self.valor = valor.upper()
        elif isinstance(valor, int):
            self.valor = hex(valor)[2:].upper() if valor >= 0 else "-" + hex(abs(valor))[2:].upper()
        else:
            raise ValueError("El valor debe ser una cadena hexadecimal o un entero")
        super().__init__(self.valor)
    
    def a_decimal(self) -> int:
        if self.valor.startswith('-'):
            return -int(self.valor[1:], 16)
        else:
            return int(self.valor, 16)
    
    def a_binario(self) -> str:
        decimal = self.a_decimal()
        if decimal == 0:
            return "0"
        elif decimal < 0:
            return "-" + bin(abs(decimal))[2:]
        else:
            return bin(decimal)[2:]
    
    def a_octal(self) -> str:
        decimal = self.a_decimal()
        if decimal == 0:
            return "0"
        elif decimal < 0:
            return "-" + oct(abs(decimal))[2:]
        else:
            return oct(decimal)[2:]
    
    def a_hexadecimal(self) -> str:

        return self.valor
    
    def a_romano(self) -> str:
        decimal = self.a_decimal()
        if decimal == 0:
            return "N"
        elif decimal < 0:
            return "-" + self._decimal_a_romano(abs(decimal))
        else:
            return self._decimal_a_romano(decimal)
    
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
        return Hexadecimal(valor_decimal)
