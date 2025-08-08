from Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Triángulito")
        self.base = base
        self.altura = altura

    def calcular_area_figura(self):
        return (self.base * self.altura) / 2
