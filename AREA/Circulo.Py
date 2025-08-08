from Calc_A import Figura
class circulo(Figura):
    def _init_(self,radio):
        self.radio=radio
     
    def calcular_area(self):
        print (3.141516*(self.radio**2))