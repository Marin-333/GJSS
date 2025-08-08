class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def mostrar_nombre(self):
        print("Figura: Cuadrado")

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
