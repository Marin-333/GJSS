# main.py
from identificadorn import reconocer_tipo

def menu_principal():
    print("\n¿Qué deseas hacer?")
    print("1) Convertir")
    print("2) Sumar")
    print("3) Multiplicar")
    print("4) Salir")
    return input("Elige una opción: ").strip()

def menu_conversion():
    print("\n¿A qué formato quieres convertir?")
    print("1) Decimal")
    print("2) Binario")
    print("3) Octal")
    print("4) Hexadecimal")
    print("5) Entero")
    print("6) Romano")
    return input("Elige una opción: ").strip()

def convertir_a(numero, opcion):
    """Devuelve SOLO el formato elegido por el usuario."""
    try:
        if opcion == "1":   # Decimal
            return str(numero.to_decimal())
        elif opcion == "2": # Binario (limpio, sin 0b)
            return numero.a_binario()
        elif opcion == "3": # Octal (limpio, sin 0o)
            return numero.a_octal()
        elif opcion == "4": # Hex (limpio, sin 0x, mayúsculas)
            return numero.a_hexadecimal()
        elif opcion == "5": # Entero
            return str(numero.a_entero())
        elif opcion == "6": # Romano
            return numero.a_romano()
        else:
            return "Opción de conversión no válida."
    except Exception:
        return "No se pudo convertir ese valor."

def leer_numero(mensaje="Ingrese un número (ej: 15, 0b101, 0o17, 0xF, XV): "):
    """Pide un número hasta que sea válido. Nunca lanza traceback al usuario."""
    while True:
        try:
            valor = input(mensaje).strip()
            num = reconocer_tipo(valor)   # puede devolver None si no reconoce
            if not num:
                print("Entrada no válida. Intenta de nuevo.")
                continue
            # Validar que realmente se pueda convertir
            _ = num.to_decimal()
            return num
        except Exception:
            print("Entrada no válida. Intenta de nuevo.")

def main():
    # Pedimos el primer número (con validación robusta)
    numero = leer_numero()
    print(f"Tipo detectado: {numero.tipo()}")

    while True:
        opcion = menu_principal()

        if opcion == "1":  # Convertir
            op_conv = menu_conversion()
            print(f"\nResultado: {convertir_a(numero, op_conv)}")

        elif opcion in ("2", "3"):  # Sumar o Multiplicar
            otro = leer_numero("Ingrese otro número: ")
            try:
                a, b = numero.to_decimal(), otro.to_decimal()
                if opcion == "2":
                    res, op_txt = a + b, "suma"
                else:
                    res, op_txt = a * b, "multiplicación"

                print(f"\nResultado en decimal de la {op_txt}: {res}")

                # Preguntar si desea convertir el resultado (solo al formato elegido)
                while True:
                    sub = input("\n¿Quieres convertir el resultado? 1) Sí  2) No: ").strip()
                    if sub == "1":
                        from decimaln import Decimal
                        dec_num = Decimal(str(res))
                        op_conv = menu_conversion()
                        print(f"Resultado convertido: {convertir_a(dec_num, op_conv)}")
                    elif sub == "2":
                        break
                    else:
                        print("Opción no válida.")
            except Exception:
                print("Ocurrió un problema al operar los números. Intenta de nuevo.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
