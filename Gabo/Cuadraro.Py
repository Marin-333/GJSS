from Calc_A import Figura
class cuadrado(Figura):
    def _init_(self,lado):
        self.lado=lado

    def calcular_area(self):
        print(self.lado**2)