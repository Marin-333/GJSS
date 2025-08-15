from api_numeros import APINumeros
import json

def mostrar_menu():
    print("\n" + "-"*60)
    print("   API DE NÚMEROS - SISTEMA DE CONVERSIÓN")
    print("-"*60)
    print("1. Realizar operación (suma o multiplicación)")
    print("2. Convertir número a otro tipo")
    print("3. Mostrar número en todos los formatos")
    print("4. Ver ejemplos de cada tipo")
    print("5. Validar entrada")
    print("6. Salir")
    print("-"*60)


def mostrar_tipos_disponibles(api):
    tipos = api.obtener_tipos_disponibles()
    print("\nTipos de números disponibles:")
    for i, tipo in enumerate(tipos, 1):
        print(f"  {i}. {tipo.capitalize()}")



def realizar_operacion_interactiva(api):
    print("\n _REALIZAR OPERACIÓN_")
    
    try:
        print("Primer número:")
        mostrar_tipos_disponibles(api)
        tipo1_idx = int(input("\nSeleccione el tipo del primer número (1-5): ")) - 1
        tipos = api.obtener_tipos_disponibles()
        
        if 0 <= tipo1_idx < len(tipos):
            tipo1 = tipos[tipo1_idx]
            valor1 = input(f"Ingrese el valor para {tipo1}: ")
            numero1 = api.crear_numero(tipo1, valor1)
            print(f"Número {tipo1} creado: {numero1}")
        else:
            print("Opción no válida")
            return
        
        print("\nSegundo número:")
        mostrar_tipos_disponibles(api)
        tipo2_idx = int(input("\nSeleccione el tipo del segundo número (1-5): ")) - 1
        
        if 0 <= tipo2_idx < len(tipos):
            tipo2 = tipos[tipo2_idx]
            valor2 = input(f"Ingrese el valor para {tipo2}: ")
            numero2 = api.crear_numero(tipo2, valor2)
            print(f"Número {tipo2} creado: {numero2}")
        else:
            print("Opción no válida")
            return
        
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Multiplicación")
        
        opcion = input("Seleccione la operación (1-2): ")
        
        if opcion == "1":
            resultado = api.realizar_operacion(numero1, numero2, "suma")
            print(f"\nResultado de la suma: {resultado}")
        elif opcion == "2":
            resultado = api.realizar_operacion(numero1, numero2, "multiplicacion")
            print(f"\nResultado de la multiplicación: {resultado}")
        else:
            print("Opción no válida")
            
    except Exception as e:
        print(f"Error: {e}")

def convertir_numero_interactivo(api):
    print("\n _CONVERTIR NÚMERO_")
    
    try:
        print("Número a convertir:")
        mostrar_tipos_disponibles(api)
        tipo_idx = int(input("\nSeleccione el tipo del número (1-5): ")) - 1
        tipos = api.obtener_tipos_disponibles()
        
        if 0 <= tipo_idx < len(tipos):
            tipo = tipos[tipo_idx]
            valor = input(f"Ingrese el valor para {tipo}: ")
            numero = api.crear_numero(tipo, valor)
            print(f"Número {tipo} creado: {numero}")
        else:
            print("Opción no válida")
            return
        
        print("\nTipo destino:")
        mostrar_tipos_disponibles(api)
        tipo_idx = int(input("Seleccione el tipo destino (1-5): ")) - 1
        tipos = api.obtener_tipos_disponibles()
        
        if 0 <= tipo_idx < len(tipos):
            tipo_destino = tipos[tipo_idx]
            resultado = api.convertir_numero(numero, tipo_destino)
            print(f"\nConversión exitosa: {resultado}")
        else:
            print("Opción no válida")
            
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def mostrar_conversiones_interactivo(api):
    print("\n MOSTRAR CONVERSIONES ")
    
    mostrar_tipos_disponibles(api)
    tipo_idx = int(input("\nSeleccione el tipo del número (1-5): ")) - 1
    tipos = api.obtener_tipos_disponibles()
    
    if 0 <= tipo_idx < len(tipos):
        tipo = tipos[tipo_idx]
        valor = input(f"Ingrese el valor para {tipo}: ")
        numero = api.crear_numero(tipo, valor)
        print(f"Número {tipo} creado: {numero}")
        
        conversiones = api.mostrar_conversiones(numero)
        print(f"\nConversiones para {numero}:")
        for tipo, valor in conversiones.items():
            print(f"  {tipo.capitalize()}: {valor}")
    else:
        print("Opción no válida")

def mostrar_ejemplos(api):
    print("\n- EJEMPLOS DE CADA TIPO -")
    ejemplos = api.obtener_ejemplos()
    for tipo, ejemplo in ejemplos.items():
        print(f"\n{tipo.capitalize()}: {ejemplo}")
        try:
            numero = api.crear_numero(tipo, ejemplo)
            conversiones = api.mostrar_conversiones(numero)
            print("  Conversiones:")
            for tipo_conv, valor in conversiones.items():
                print(f"    {tipo_conv}: {valor}")
        except Exception as e:
            print(f"  Error: {e}")

def validar_entrada_interactivo(api):
    print("\n- VALIDAR ENTRADA -")
    mostrar_tipos_disponibles(api)
    try:
        tipo_idx = int(input("\nSeleccione el tipo de número (1-5): ")) - 1
        tipos = api.obtener_tipos_disponibles()
        
        if 0 <= tipo_idx < len(tipos):
            tipo = tipos[tipo_idx]
            valor = input(f"Ingrese el valor para validar en {tipo}: ")
            
            if api.validar_entrada(tipo, valor):
                print(f"El valor '{valor}' es válido para {tipo}")

            else:
                print(f"El valor '{valor}' NO es válido para {tipo}")
        else:
            print("Opción no válida")
            
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def main():
    print("Iniciando API de Números...")
    
  
    api = APINumeros()
    
    print("API inicializada correctamente")
    print(f"Tipos disponibles: {', '.join(api.obtener_tipos_disponibles())}")
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSeleccione una opción (1-6): ")
            
            if opcion == "1":
                realizar_operacion_interactiva(api)
            elif opcion == "2":
                convertir_numero_interactivo(api)
            elif opcion == "3":
                mostrar_conversiones_interactivo(api)
            elif opcion == "4":
                mostrar_ejemplos(api)
            elif opcion == "5":
                validar_entrada_interactivo(api)
            elif opcion == "6":
                print("\n¡Gracias por usar la calculadora de Números!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n¡Vuelve pronto!")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
