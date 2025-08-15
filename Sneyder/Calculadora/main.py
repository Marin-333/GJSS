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
    if opcion == "1":
        return str(numero.to_decimal())
    elif opcion == "2":
        return numero.a_binario()
    elif opcion == "3":
        return numero.a_octal()
    elif opcion == "4":
        return numero.a_hexadecimal()
    elif opcion == "5":
        return str(numero.a_entero())
    elif opcion == "6":
        return numero.a_romano()
    else:
        return "Opción de conversión no válida."

def leer_numero(mensaje="Ingrese un número (ej: 15, 0b101, 0o17, 0xF, XV): "):
    while True:
        valor = input(mensaje).strip()
        num = reconocer_tipo(valor)
        if num:
            return num
        print("Entrada no válida. Intenta de nuevo.")

def main():
    numero = leer_numero()
    print(f"Tipo detectado: {numero.tipo()}")

    while True:
        opcion = menu_principal()

        if opcion == "1":  # Convertir
            op_conv = menu_conversion()
            print(f"\nResultado: {convertir_a(numero, op_conv)}")

        elif opcion in ("2", "3"):  # Sumar o Multiplicar
            otro = leer_numero("Ingrese otro número: ")
            a, b = numero.to_decimal(), otro.to_decimal()
            if opcion == "2":
                res, op_txt = a + b, "suma"
            else:
                res, op_txt = a * b, "multiplicación"
            print(f"\n✅ Resultado en decimal de la {op_txt}: {res}")

            # Convertir resultado si se desea
            while True:
                sub = input("\n¿Quieres convertir el resultado? 1) Sí  2) No: ").strip()
                if sub == "1":
                    # Reuso de conversiones creando un Decimal temporal
                    from decimaln import Decimal
                    dec_num = Decimal(str(res))
                    op_conv = menu_conversion()
                    print(f"Resultado convertido: {convertir_a(dec_num, op_conv)}")
                elif sub == "2":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
