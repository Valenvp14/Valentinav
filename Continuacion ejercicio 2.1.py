class Vehiculo:  # clase mas abstracta
    # este es el constructor de la clase
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self. modelo = modelo
        self.anio = anio
        print("Vehiculo Creado")

    def encender(self):
        print("Estoy listo para llevarte")

    def arrancarmoto(self):
        print("encendido y listo")

class Automovil(Vehiculo):  # herencia simple: Automovil extiende a Vehiculo
    __galonesGasolina = 0
    transmisionManual = True

    def encender(self):  # ejemplo de Polimorfismo - overriding
        print("Listo para llevarte en este", self.modelo)

    def arrancar(self):
        print("raaaahh rahh!!")

    def tocarCorneta(self):
        print("beep beep!")

    def echarGasolina(self, vGalones):  # Encapsulamiento - esto es un setter
        if vGalones <= 1:
            print("con un solo galon, no llegas a ninguna parte")
        else:
            self.__galonesGasolina = vGalones

    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
        print("Ud. tiene:", self.__galonesGasolina, "galones de Gasolina")

class moto(Vehiculo):
    __rueda = 0
    __gasolina = 0

    def prender(self):
      print("Ready")

    def arrancarmoto(self):
        print("no tengo ruedas para llevarte en este", self.marca)

    def echarGasolina(self, vGalones):  # Encapsulamiento - esto es un setter
            if vGalones <= 1:
                print("con un solo galon de gasolina no llegaras a nungun lado")
            else:
                if vGalones>=0 and vGalones<=7:
                   print("necesitas echar gasolina para seguir")
                   self.__galonesGasolina = vGalones
                else:
                    print("no puedes echar mas de 7 galones de gasolina")


    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
            print("Ud. tiene:", self.__galonesGasolina, "galones de Gasolina")

    def comprarrueda(self, rueda):
        if rueda <= 1:
            print("con tres ruedas no puedes moverte")
        else:
            if rueda>=0 and rueda<=5:
                print("necesitas ruedas para seguir andando")
                self.__rueda = rueda


    def cuantasruedasnecesito(self):
        print("usted necesita", self.__rueda, "ruedas para la moto")


# instanciando la clase Vehiculo-Automovil
miCarro = Automovil("Chevrolet", "Aveo", "2015")
miCarro.encender()
miCarro.arrancar()
miCarro.tocarCorneta()
miCarro.cuantaGasolinaHay()
miCarro.echarGasolina(100)
miCarro.cuantaGasolinaHay()

mimoto = moto("YAMAHA", "KODIAK700", "2021")
mimoto.prender()
mimoto.arrancarmoto()
mimoto.echarGasolina(6)
mimoto.cuantaGasolinaHay()
mimoto.cuantasruedasnecesito()
mimoto.comprarrueda(4)
mimoto.cuantasruedasnecesito()


