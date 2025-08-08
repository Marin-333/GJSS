import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def mostrar_nombre(self):
        print("Figura: Círculo")

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio
