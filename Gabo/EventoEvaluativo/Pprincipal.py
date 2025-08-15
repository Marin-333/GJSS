from Decimal import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from CalcU import CalculadoraUniversal

def crear_numero(tipo: str, valor: str):
    clases = {
        'decimal': NumeroDecimal,
        'binario': NumeroBinario,
        'octal': NumeroOctal,
        'hexadecimal': NumeroHexadecimal
    }
    clase = clases.get(tipo.lower())
    if clase:
        return clase(valor)
    else:
        raise ValueError("Tipo de número no reconocido")

def main():
    print("Bienvenido a la Calculadora Numérica Universal")
    print("Tipos disponibles: decimal, binario, octal, hexadecimal")

    tipo1 = input("Tipo del primer número: ")
    valor1 = input("Valor del primer número: ")
    tipo2 = input("Tipo del segundo número: ")
    valor2 = input("Valor del segundo número: ")
    operacion = input("Operación (+, -): ")

    try:
        num1 = crear_numero(tipo1, valor1)
        num2 = crear_numero(tipo2, valor2)
        resultado = CalculadoraUniversal.operar(num1, num2, operacion)
        print(f"\nResultado en base {tipo1}: {resultado}")
        print(f" Equivalente en decimal: {resultado.a_decimal()}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
