from abc import (ABC, abstractmethod)


class Cuentas(ABC):
    __saldo = 0

    def __init__(self, capitalinical, tasa, tiempo):
        self.tasa = tasa
        self.tiempo = tiempo
        self.capitalinicial = capitalinical

    def ConsultarSaldo(self):  # getter
        vResult = self.__saldo
        print("tienes de saldo", self.__saldo)

    @abstractmethod
    def AbonodeIntereses(self, bono):  # setter
        if bono % 0.10:
            print("el interes simple tiene que ser", self.capitalinicial * self.tasa * self.tiempo)
        else:
            self.__saldo = bono

    def Depositar(self):
        print("cuanto desea depositar")

    def Retirar(self):
        print("desea retirar esa cantidad")


class PlazoFijo(Cuentas):

    def ConsultarSaldo(self):
        print("su saldo inicial es", self.capitalinicial)

    def AbonodeIntereses(self, bono):
        __bono = 4
        bono *= __bono
        self.__saldo += bono


    def Depositar(self):
        print("usted realizo el deposito")

    def Retirar(self):
        pass


class CuentaAhorro(Cuentas):

    def ConsultarSaldo(self):
        print("usted tiene un saldo de", self.capitalinicial)

    def AbonodeIntereses(self, bono):
        print("su a bono es de")


PlazoFijo1 = PlazoFijo("100", "4", "60")
PlazoFijo1.ConsultarSaldo()
PlazoFijo1.AbonodeIntereses(10)
PlazoFijo1.ConsultarSaldo()

CuentaAhorro = CuentaAhorro("20", "2", "40")
CuentaAhorro.ConsultarSaldo()
CuentaAhorro.AbonodeIntereses()
CuentaAhorro.ConsultarSaldo()
