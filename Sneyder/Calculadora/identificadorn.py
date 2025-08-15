from binarion import Binario
from decimaln import Decimal
from hexadecimaln import Hexadecimal
from octaln import Octal
from romanosn import Romano

def reconocer_tipo(valor: str):
    valor = valor.strip()
    try:
        v = valor.lower()
        if v.startswith("0x"):
            return Hexadecimal(valor)
        elif v.startswith("0o"):
            return Octal(valor)
        elif v.startswith("0b"):
            return Binario(valor)
        elif valor.isdigit():
            return Decimal(valor)
        elif all(c in "IVXLCDMivxlcdm" for c in valor) and valor:
            return Romano(valor)
        else:
            return None
    except ValueError:
        print("Formato no válido.")
        return None
