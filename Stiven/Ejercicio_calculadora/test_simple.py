#!/usr/bin/env python3
"""
Pruebas simples para la API de Números
"""

from api_numeros import APINumeros

def test_basico():
    """Prueba básica de funcionamiento"""
    print("🧪 PRUEBA BÁSICA DE LA API")
    print("-" * 40)
    
    try:
        # Crear API
        api = APINumeros()
        print("✅ API creada exitosamente")
        
        # Verificar tipos disponibles
        tipos = api.obtener_tipos_disponibles()
        print(f"✅ Tipos disponibles: {tipos}")
        
        # Crear números de diferentes tipos
        decimal = api.crear_numero('decimal', 42)
        binario = api.crear_numero('binario', '101010')
        romano = api.crear_numero('romano', 'XLII')
        
        print(f"✅ Decimal: {decimal}")
        print(f"✅ Binario: {binario}")
        print(f"✅ Romano: {romano}")
        
        # Probar conversiones
        print(f"\nConversiones del decimal 42:")
        conversiones = decimal.mostrar_todos_tipos()
        for tipo, valor in conversiones.items():
            print(f"  {tipo}: {valor}")
        
        # Probar operaciones
        suma = decimal.suma(binario)
        print(f"\n✅ Suma: {decimal} + {binario} = {suma}")
        
        multiplicacion = decimal.multiplicacion(romano)
        print(f"✅ Multiplicación: {decimal} × {romano} = {multiplicacion}")
        
        print("\n🎉 ¡Todas las pruebas básicas pasaron!")
        
    except Exception as e:
        print(f"❌ Error en las pruebas: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_basico()
