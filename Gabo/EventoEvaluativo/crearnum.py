from Decimal import NDecimal
from Binario import NBinario
from Hexadecimal import NuHexa
from Octal import NuOctal

def crear_numero(tipo, valor):
    if tipo== "decimal":
        return NDecimal(valor)
    elif tipo== "binario":
        return NBinario(valor)
    elif tipo== "hexadecimal":
        return NuHexa(valor)
    elif tipo== "octal":
        return NuOctal(valor)
    else:
        raise print("Ese tipo no es valido")