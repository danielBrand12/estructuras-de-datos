class NodoDoble:
    def __init__(self, d):
        self.dato = d
        self.liga_derecha = None
        self.liga_izquierda = None

    def retorna_dato(self):
        return self.dato

    def retorna_liga_derecha(self):
        return self.liga_derecha

    def retorna_liga_izquierda(self):
        return self.liga_izquierda

    def asigna_dato(self, d):
        self.dato = d

    def asigna_liga_derecha(self, x):
        self.liga_derecha = x

    def asigna_liga_izquierda(self, x):
        self.liga_izquierda = x
