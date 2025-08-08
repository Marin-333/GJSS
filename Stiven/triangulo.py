class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mostrar_nombre(self):
        print("Figura: Triángulo")

    def area(self):
        return (self.base * self.altura) / 2
