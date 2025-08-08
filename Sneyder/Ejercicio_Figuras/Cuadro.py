from Figura import Figura

class Cuadro(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrito")
        self.lado = lado

    def calcular_area_figura(self):
        return self.lado * self.lado
