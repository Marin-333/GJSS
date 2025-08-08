from Figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculito")
        self.radio = radio

    def calcular_area_figura(self):
        pi = 3.14
        return pi * self.radio ** 2
