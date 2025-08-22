class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area_figura(self):
        raise NotImplementedError("Aca es donde se sobreescribe el metodo por las clases hijas :)")
