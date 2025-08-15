from cuadrado import Cuadrado
from triangulo import Triangulo
from circulo import Circulo

print("=== Figuras Geométricas ===\n")

c = Cuadrado(4)
c.mostrar_nombre()
print(f"Área: {c.area()}")
print(f"Perímetro: {c.perimetro()}\n")

t = Triangulo(5, 3)
t.mostrar_nombre()
print(f"Área: {t.area()}\n")

ci = Circulo(2)
ci.mostrar_nombre()
print(f"Área: {ci.area():.2f}")
print(f"Circunferencia: {ci.circunferencia():.2f}")
