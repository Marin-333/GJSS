from Calc_A import Figura
class triangulo(Figura):
    def _init_(self,altura,base):
        self.altura=altura
        self.base=base

    def calcular_area(self):
        print((self.altura * self.base) / 2)  