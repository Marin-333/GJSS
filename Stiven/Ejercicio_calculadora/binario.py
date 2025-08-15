from numero_abstracto import NumeroAbstracto

class Binario(NumeroAbstracto):
      
    def __init__(self, valor):
        if isinstance(valor, str):
            if not all(bit in '01' for bit in valor):
                raise ValueError("El valor debe ser una cadena binaria válida (solo 0s y 1s)")
            self.valor = valor
        elif isinstance(valor, int):
            self.valor = bin(valor)[2:] if valor >= 0 else "-" + bin(abs(valor))[2:]
        else:
            raise ValueError("El valor debe ser una cadena binaria o un entero")
        super().__init__(self.valor)
    
    def a_decimal(self) -> int:
        if self.valor.startswith('-'):
            return -int(self.valor[1:], 2)
        else:
            return int(self.valor, 2)
    
    def a_binario(self) -> str:
        return self.valor
    
    def a_octal(self) -> str:
        decimal = self.a_decimal()
        if decimal == 0:
            return "0"
        elif decimal < 0:
            return "-" + oct(abs(decimal))[2:]
        else:
            return oct(decimal)[2:]
    
    def a_hexadecimal(self) -> str:
        decimal = self.a_decimal()
        if decimal == 0:
            return "0"
        elif decimal < 0:
            return "-" + hex(abs(decimal))[2:].upper()
        else:
            return hex(decimal)[2:].upper()
    
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
        return Binario(valor_decimal)
