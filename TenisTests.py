import unittest
from Tenis import Tenis

class MyTestCase(unittest.TestCase):

    def crearPartida(self):
        partido = Tenis()
    def test_scoreinicial(self):
        partido =Tenis()
        self.assertEqual('0-0', partido.calcularPuntuacion())

    def test_15nada(self):
        partido=Tenis()
        partido.jugador1Incrementar()
        self.assertEqual('15-0', partido.calcularPuntuacion())

    def test_30nada(self):
        partido=Tenis()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        self.assertEqual('30-0', partido.calcularPuntuacion())

    def test_40nada(self):
        partido=Tenis()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        self.assertEqual('40-0', partido.calcularPuntuacion())

    def test_gana1(self):
        partido=Tenis()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        partido.jugador1Incrementar()
        self.assertEqual('Gana Jugador 1', partido.ganadorPunto())

    def nada15(self):
        partido=Tenis()
        partido.jugador2Incrementar()
        self.assertEqual('0-15', partido.calcularPuntuacion())



if __name__ == '__main__':
    unittest.main()
