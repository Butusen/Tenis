class Tenis:
    def __init__(self):
        self.puntuacionjug1= 0
        self.map = {
            0: '0',
            1: '15',
            2: '30',
            3: '40'
        }
    def calcularPuntuacion(self):
        return f'{self.map[self.puntuacionjug1]}-0'
    def ganadorPunto(self):
        if self.puntuacionjug1 == 4:
            return "Gana Jugador 1"
    def jugador1Incrementar(self):
        self.puntuacionjug1 += 1









