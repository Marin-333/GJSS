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
            # Validación de hexadecimal (0-9 y A-F)
            if all(c in "0123456789abcdef" for c in v[2:]):
                return Hexadecimal(valor)
            else:
                print("Error: número hexadecimal inválido.")
                return None

        elif v.startswith("0o"):
            # Validación de octal (solo 0-7)
            if all(c in "01234567" for c in v[2:]):
                return Octal(valor)
            else:
                print("Error: número octal inválido. Usa solo dígitos del 0 al 7.")
                return None

        elif v.startswith("0b"):
            # Validación de binario (solo 0 y 1)
            if all(c in "01" for c in v[2:]):
                return Binario(valor)
            else:
                print("Error: número binario inválido. Usa solo 0 y 1.")
                return None

        elif valor.isdigit():
            return Decimal(valor)

        elif all(c in "IVXLCDMivxlcdm" for c in valor) and valor:
            return Romano(valor)

        else:
            print("Error: formato no reconocido. Intenta de nuevo.")
            return None

    except Exception:
        print("Error: dato inválido, intenta de nuevo.")
        return None
