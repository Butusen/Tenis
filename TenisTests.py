import unittest
from Tenis import Tenis

class MyTestCase(unittest.TestCase):

    def crearPartida(self):
        partido = Tenis()
    def test_scoreinicial(self):
        partido =Tenis()
        self.assertEqual("0-0", partido.calcularPuntuacion())

    def test_15nada(self):
        partido=Tenis()
        self.assertEqual("15-0", partido.calcularPuntuacion())


if __name__ == '__main__':
    unittest.main()
