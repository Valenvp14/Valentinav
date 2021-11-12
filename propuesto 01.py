class Triangulo:

    def __init__(self, altura, base):
        print("intanciando esta clase")

        self.altura = altura
        self.base = base

    def muestraLaAltura(self):
        print("la altura del triangulo es:", self.altura)

    def muestraLaBase(self):
        print("la base del triangulo es:", self.base)

    def calcularlaSuperficie(self):
        print("la superficie del triangulo es:", self.base * self.altura / 2)

Triangulo1 = Triangulo(12, 4)
Triangulo1.muestraLaAltura()

Triangulo2 = Triangulo(12, 4)
Triangulo2.muestraLaBase()

Triangulo3 = Triangulo(12, 4)
Triangulo3.calcularlaSuperficie()




