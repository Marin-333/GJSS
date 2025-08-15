from decimal import Decimal
from binario import Binario
from octal import Octal
from hexadecimal import Hexadecimal
from romano import Romano

class APINumeros:

    
    def __init__(self):
        self.tipos_disponibles = {
            'decimal': Decimal,
            'binario': Binario,
            'octal': Octal,
            'hexadecimal': Hexadecimal,
            'romano': Romano
        }
    
    def crear_numero(self, tipo, valor):

        if tipo not in self.tipos_disponibles:
            raise ValueError(f"Tipo no válido. Tipos disponibles: {list(self.tipos_disponibles.keys())}")
        
        try:
            clase_numero = self.tipos_disponibles[tipo]
            return clase_numero(valor)
        except Exception as e:
            raise ValueError(f"Error al crear número {tipo} con valor {valor}: {str(e)}")
    
    def obtener_tipos_disponibles(self):
        return list(self.tipos_disponibles.keys())
    
    def convertir_numero(self, numero, tipo_destino):
           
        if tipo_destino not in self.tipos_disponibles:
            raise ValueError(f"Tipo destino no válido: {tipo_destino}")
        
        clase_destino = self.tipos_disponibles[tipo_destino]
        valor_decimal = numero.a_decimal()
        return clase_destino(valor_decimal)
    
    def realizar_operacion(self, numero1, numero2, operacion):
        
      

        if operacion == 'suma':
            return numero1.suma(numero2)
        elif operacion == 'multiplicacion':
            return numero1.multiplicacion(numero2)
        else:
            raise ValueError("Operación no válida. Use 'suma' o 'multiplicacion'")
    
    def mostrar_conversiones(self, numero):
        return numero.mostrar_todos_tipos()
    
    def validar_entrada(self, tipo, valor):

        try:
            if tipo == 'decimal':
                int(valor)
            else:
                self.crear_numero(tipo, valor)
            return True
        except:
            return False
    
    def obtener_ejemplos(self):
        ejemplos = {}
        for tipo in self.tipos_disponibles:
            if tipo == 'decimal':
                ejemplos[tipo] = 42
            elif tipo == 'binario':
                ejemplos[tipo] = "101010"
            elif tipo == 'octal':
                ejemplos[tipo] = "52"
            elif tipo == 'hexadecimal':
                ejemplos[tipo] = "2A"
            elif tipo == 'romano':
                ejemplos[tipo] = "XLII"
        
        return ejemplos
