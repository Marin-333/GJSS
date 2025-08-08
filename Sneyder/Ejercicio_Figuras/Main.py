from Cuadro import Cuadro
from Triangulo import Triangulo
from Circulo import Circulo

cuadro = Cuadro(4)
triangulo = Triangulo(5, 6)
circulo = Circulo(8)

print(f"Área del cuadrito: {cuadro.calcular_area_figura()}")
print(f"Área del triángulito: {triangulo.calcular_area_figura()}")
print(f"Área del círculito: {circulo.calcular_area_figura()}")
