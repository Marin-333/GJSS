from numero_abstracto import NumeroAbstracto

class Romano(NumeroAbstracto):
    def __init__(self, valor):
        if isinstance(valor, str):

            if not self._es_romano_valido(valor):
                raise ValueError("El valor debe ser una cadena romana válida")
            self.valor = valor.upper()
        elif isinstance(valor, int):
            if valor == 0:
                self.valor = "N"
            elif valor < 0:
                self.valor = "-" + self._decimal_a_romano(abs(valor))
            else:
                self.valor = self._decimal_a_romano(valor)
        else:
            raise ValueError("El valor debe ser una cadena romana o un entero")
        super().__init__(self.valor)
    
    def a_decimal(self) -> int:
        if self.valor == "N":
            return 0
        elif self.valor.startswith('-'):
            return -self._romano_a_decimal(self.valor[1:])
        else:
            return self._romano_a_decimal(self.valor)
    
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
        decimal = self.a_decimal()
        if decimal == 0:
            return "0"
        elif decimal < 0:
            return "-" + hex(abs(decimal))[2:].upper()
        else:
            return hex(decimal)[2:].upper()
    
    def a_romano(self) -> str:
        return self.valor
    
    def _romano_a_decimal(self, romano):
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        resultado = 0
        anterior = 0
        
        for letra in reversed(romano):
            actual = valores[letra]
            if actual >= anterior:
                resultado += actual
            else:
                resultado -= actual
            anterior = actual
        
        return resultado
    
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
    
    def _es_romano_valido(self, romano):
        if not romano:
            return False
        
        letras_validas = set('IVXLCDMN')
        if not all(letra in letras_validas for letra in romano.upper()):
            return False
        
        romano = romano.upper()
        
        for letra in 'IXCM':
            if romano.count(letra) > 3:
                return False
        
        for letra in 'VLD':
            if romano.count(letra) > 1:
                return False
        
        return True
    
    def _crear_instancia_mismo_tipo(self, valor_decimal):
        return Romano(valor_decimal)
