#!/usr/bin/python3

class rectangulo:
    # constructor de la clase.  Se ejecuta
    # cuando la instanciamos
    def __init__(self, altura, ancho):
        print("Instanciando esta clase")

        # Atributos
        self.altura = altura
        self.ancho = ancho

        # Metodos
    def muestraElAncho(self):
        print("el ancho del rectangulo es:", self.ancho)

    def muestraLaAltura(self):
        print("la altura del rectangulo es:", self.altura)

    def calculaLaSuperficie(self):
        print("la superficie del rectangulo es:", self.altura * self.ancho)


# vamos a instanciar la clase rectangulo
# tantas veces como rectangulos necesitemos
rectangulo1 = rectangulo(12, 3)
rectangulo1.muestraElAncho()

# vamos a instanciar el
# segundo rectangulo
rectangulo2 = rectangulo(12, 3)
rectangulo2.muestraLaAltura()

rectangulo3 = rectangulo(12, 3)
rectangulo3.calculaLaSuperficie()



