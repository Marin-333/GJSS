from abc import ABC, abstractmethod

class NumeroAbstracto(ABC):
    def __init__(self, valor):
        self.valor = valor
    
    @abstractmethod
    def a_decimal(self) -> int:
        pass
    
    @abstractmethod
    def a_binario(self) -> str:
        pass
    
    @abstractmethod
    def a_octal(self) -> str:
        pass
    
    @abstractmethod
    def a_hexadecimal(self) -> str:
        pass
    
    @abstractmethod
    def a_romano(self) -> str:
        pass
    
    def suma(self, otro):
        if isinstance(otro, NumeroAbstracto):
            resultado_decimal = self.a_decimal() + otro.a_decimal()
            return self._crear_instancia_mismo_tipo(resultado_decimal)
        else:
            raise TypeError("Solo se pueden sumar objetos de tipo NumeroAbstracto")
    
    def multiplicacion(self, otro):
        if isinstance(otro, NumeroAbstracto):
            resultado_decimal = self.a_decimal() * otro.a_decimal()
            return self._crear_instancia_mismo_tipo(resultado_decimal)
        else:
            raise TypeError("Solo se pueden multiplicar objetos de tipo NumeroAbstracto")
    
    @abstractmethod
    def _crear_instancia_mismo_tipo(self, valor_decimal):
        pass
    
    def mostrar_todos_tipos(self):
        return {
            'decimal': self.a_decimal(),
            'binario': self.a_binario(),
            'octal': self.a_octal(),
            'hexadecimal': self.a_hexadecimal(),
            'romano': self.a_romano()
        }
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.valor})"
    
    def __repr__(self):
        return self.__str__()
