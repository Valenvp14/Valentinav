class figuras:
    def formula(self):
        print("NO TODAS LAS FIGURAS TIENEN LA MISMA FORMULA")

class Triangulo(figuras):
    def formula(self):
        print("la formula del triangulo es: base * altura / 2")

class cuadrado(figuras):
    def formula(self):
        print("la formula del cuadrado es: lado**2")

class circulo(figuras):
    def formula(self):
        print("la formula del circulo es: pi * radio**2")

class rectangulo(figuras):
    def formula(self):
        print("la formula del rectangulo es: base * altura")

figuras1 = figuras()
figuras1.formula()

Triangulo2 = Triangulo()
Triangulo2.formula()

cuadrado3 = cuadrado()
cuadrado3.formula()

circulo4 = circulo()
circulo4.formula()

rectangulo5 = rectangulo()
rectangulo5.formula()



