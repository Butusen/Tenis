class Tenis:
    def __init__(self):
        self.puntuacionjug1= 0
        self.puntuacionjug2=0
        self.map = {
            0: '0',
            1: '15',
            2: '30',
            3: '40',
            4: 'Av'
        }
    def calcularPuntuacion(self):
        return f'{self.map[self.puntuacionjug1]}-{self.map[self.puntuacionjug2]}'
    def ganadorPunto(self):
        if self.puntuacionjug1 == 4:
            return "Gana Jugador 1"
        elif self.puntuacionjug2 == 4:
            return "Gana Jugador 2"
    def jugador1Incrementar(self):
        self.puntuacionjug1 += 1

    def jugador1Restar(self):
        self.puntuacionjug1 -= 1

    def jugador2Incrementar(self):
        self.puntuacionjug2 += 1








