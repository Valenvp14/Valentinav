from abc import (ABC, abstractmethod)


class animales(ABC):
    __vacunado = False

    def __init__(self, nombre, raza, edad, fecha):
        self.nombre = nombre
        self.__edad = edad
        self.raza = raza
        self.fecha = fecha

    def VacunasGatuna(self):
        print("GXXXX")

    def VacunaPerruna(self):
        print("PXXXX")

    @abstractmethod
    def AplicarVacuna(self):
        print("al paciente le corresponde")



class Perro(animales):

    def AplicarVacuna(self,):
        __vacuna = True
           print("al perro le corresponder esta vacuna Pxxx")

    def Hablar(self):
        print("GUAU GUAU")

    def VacunaPerruna(self):
        print("le corresponde esta vacuna")


class Gato(animales):

    def Hablar(self):
        print("miau miau")

    def aplicarvacuna(self, vacuna):
        print("al paciente le corresponde la vacuna GXXX")

    def VacunasGatuna(self):
        print("al paciente le corresponde esta vacuna")


miperro = Perro("MIMI, GOLDEN, 6, 2015")
miperro.Hablar()
miperro.AplicarVacuna()

migato = Gato("orion, mestizo, 1, 2020")
migato.AplicarVacuna()
migato.Hablar()

