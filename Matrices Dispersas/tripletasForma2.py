from tripleta import Tripleta
from nodoDoble import NodoDoble
from matEnTripletas import MatEnTripletas


class MatrizForma2:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        t = Tripleta(m, n, None)
        self.mat = NodoDoble(t)
        tx = Tripleta(None, None, None)
        x = NodoDoble(tx)
        x.asigna_liga_derecha(x)
        x.asigna_liga_izquierda(x)
        self.mat.asigna_liga_derecha(x)

    def nodoCabeza(self):
        return self.mat.retorna_liga_derecha()

    def primerNodo(self):
        t = self.mat.retorna_dato()
        p = t.get_value()
        return p

    def esVacia(self):
        p = self.mat.getLigaDer()
        return p.retorna_liga_izquierda() == p and p.retorna_liga_derecha() == p

    def finDeRecorrido(self, p):
        return p == self.nodoCabeza()

    def muestraMatriz(self):
        q = self.nodoCabeza().retorna_liga_derecha()
        while not self.finDeRecorrido(q):
            tq = q.retorna_dato()
            f = tq.get_fila()
            c = tq.get_col()
            v = tq.get_value()
            print(f, c, v)
            q = q.retorna_liga_derecha()

    def conectaPorFilasForma2(self, x):
        tx = x.retorna_dato()
        p = self.nodoCabeza()
        anterior = p
        q = p.retorna_liga_derecha()
        tq = q.retorna_dato()
        while q != p and tq.get_fila() < tx.get_fila():
            anterior = q
            q = q.retorna_liga_derecha()
            tq = q.retorna_dato()
        while q != p and tq.get_fila() == tx.get_fila() and tq.get_col() < tx.get_col():
            anterior = q
            q = q.retorna_liga_derecha()
            tq = q.retorna_dato()
        anterior.asigna_liga_derecha(x)
        x.asigna_liga_derecha(q)

    def conectaPorColumna2(self, x):
        tx = x.retorna_dato()
        p = self.nodoCabeza()
        anterior = p
        q = p.retorna_liga_izquierda()
        tq = q.retorna_dato()
        while q != p and tq.get_col() < tx.get_col():
            anterior = q
            q = q.retorna_liga_izquierda()
            tq = q.retorna_dato()
        while q != p and tq.get_col() == tx.get_col() and tq.get_fila() < tx.get_fila():
            anterior = q
            q = q.retorna_liga_izquierda()
            tq = q.retorna_dato()
        anterior.asigna_liga_izquierda(x)
        x.asigna_liga_izquierda(q)

    def aVector(self):
        q = self.nodoCabeza().retorna_liga_derecha()
        mat = MatEnTripletas(self.m, self.n, 0)
        while not self.finDeRecorrido(q):
            tq = q.retorna_dato()
            f = tq.get_fila()
            c = tq.get_col()
            v = tq.get_value()
            t = Tripleta(f, c, v)
            mat.agrega_tripleta(t)
            q = q.retorna_liga_derecha()
        return mat

    def aCuadricula(self):
        mat = []
        for i in range(self.m):
            mat.append([])
            for j in range(self.n):
                mat[i].append(0)
        q = self.nodoCabeza().retorna_liga_derecha()
        while not self.finDeRecorrido(q):
            tq = q.retorna_dato()
            f = tq.get_fila()
            c = tq.get_col()
            v = tq.get_value()
            mat[f - 1][c - 1] = v
            q = q.retorna_liga_derecha()
        return mat