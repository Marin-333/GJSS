class CalculadoraUniversal:
    @staticmethod
    def operar(a, b, operacion: str):
        if operacion == '+':
            return a + b
        elif operacion == '-':
            return a - b
       
        else:
            raise ValueError("Operación no válida")
