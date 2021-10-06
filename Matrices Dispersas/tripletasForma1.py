from nodoDoble import NodoDoble
from tripleta import Tripleta
from matEnTripletas import MatEnTripletas


class MatrizForma1:

    def __init__(self, m, n):
        self.filas = m
        self.columnas = n
        t = Tripleta(m, n, None)
        self.mat = NodoDoble(t)
        t.set_value(self.mat)
        self.mat.asigna_dato(t)

    def nodoCabeza(self):
        return self.mat

    def primerNodo(self):
        t = self.mat.retorna_dato()
        p = t.get_value()
        return p

    def getNumFila(self):
        return self.filas

    def getNumCols(self):
        return self.columnas

    def muestraMatriz(self):
        cab = self.mat
        p = self.primerNodo()
        while p != cab:
            q = p.retorna_liga_derecha()
            while q != p:
                t = q.retorna_dato()
                f = t.get_fila()
                c = t.get_col()
                v = t.get_value()
                print(f, c, v)
                q = q.retorna_liga_derecha()
            t = p.retorna_dato()
            p = t.get_value()

    def construyeNodosCabeza(self):
        t = self.mat.retorna_dato()
        m = t.get_fila()
        n = t.get_col()
        if m >= n:
            p = m
        else:
            p = n
        ultimo = self.mat
        for i in range(1, p+1):
            t = Tripleta(0, 0, self.mat)
            x = NodoDoble(t)
            x.asigna_liga_derecha(x)
            x.asigna_liga_izquierda(x)
            t = ultimo.retorna_dato()
            t.set_value(x)
            ultimo = x

    def conectaPorFilas(self, x):
        t = x.retorna_dato()
        f = t.get_fila()
        c = t.get_col()
        p = self.primerNodo()
        for i in range(1, f):
            t = p.retorna_dato()
            p = t.get_value()
        aq = p
        q = p.retorna_liga_derecha()
        t = q.retorna_dato()
        while q != p and t.get_col() < c:
            aq = q
            q = q.retorna_liga_derecha()
            t = q.retorna_dato()
        aq.asigna_liga_derecha(x)
        x.asigna_liga_derecha(q)
        t = p.retorna_dato()
        aux = (t.get_fila() + 1)
        t.set_fila(aux)
        p.asigna_dato(t)

    def conectaPorColumnas(self, x):
        tx = x.retorna_dato()
        p = self.primerNodo()
        for i in range(1, tx.get_col()):
            tp = p.retorna_dato()
            p = tp.get_value()
        anterior = p
        q = p.retorna_liga_izquierda()
        tq = q.retorna_dato()
        while (q != p) and (tq.get_fila() < tx.get_fila()):
            anterior = q
            q = q.retorna_liga_izquierda()
            tq = q.retorna_dato()
        anterior.asigna_liga_izquierda(x)
        x.asigna_liga_izquierda(q)

    def sumar(self, b):
        p = self.nodoCabeza()
        q = b.nodoCabeza()
        tp = p.getDato()
        tq = q.getDato()
        nf = tp.getFila()
        nc = tp.getColumna()
        if nf != tq.getFila() or nc != tq.getColumna():
            return None
        c = MatrizForma1(nf, nc)
        c.construyeNodosCabeza()
        pp = self.primerNodo()
        qq = b.primerNodo()
        while pp != p:
            r = pp.getLigaDer()
            s = qq.getLigaDer()
            while r != pp and s != qq:
                tr = r.getDato()
                ts = s.getDato()
                cr = tr.getColumna()
                cs = ts.getColumna()
                if cr < cs:
                    x = NodoDoble(tr)
                    c.conectaPorFilas(x)
                    c.conectaPorColumnas(x)
                    r = r.getLigaDer()
                elif cr > cs:
                    x = NodoDoble(ts)
                    c.conectaPorFilas(x)
                    c.conectaPorColumnas(x)
                    s = s.getLigaDer()
                else:
                    suma = tr.getValor() + ts.getValor()
                    if suma != 0:
                        tt = Tripleta(tr.getFila(), cr, suma)
                        x = NodoDoble(tt)
                        c.conectaPorFilas(x)
                        c.conectaPorColumnas(x)
                    r = r.getLigaDer()
                    s = s.getLigaDer()
            while r != pp:
                x = NodoDoble(r.getDato())
                c.conectaPorFilas(x)
                c.conectaPorColumnas(x)
                r = r.getLigaDer()
            while s != qq:
                x = NodoDoble(s.getDato())
                c.conectaPorFilas(x)
                c.conectaPorColumnas(x)
                s = s.getLigaDer()
            tpp = pp.getDato()
            pp = tpp.getValor()
            tqq = qq.getDato()
            qq = tqq.getValor()
        return c

    def aVector(self):
        mat = MatEnTripletas(self.filas, self.columnas, 0)
        cab = self.mat
        p = self.primerNodo()
        while p != cab:
            q = p.retorna_liga_derecha()
            while q != p:
                t = q.retorna_dato()
                f = t.get_fila()
                c = t.get_col()
                v = t.get_value()
                tripleta = Tripleta(f, c, v)
                mat.agrega_tripleta(tripleta)
                q = q.retorna_liga_derecha()
            t = p.retorna_dato()
            p = t.get_value()
        return mat

    def aCuadricula(self):
        mat = []
        for i in range(self.filas):
            mat.append([])
            for j in range(self.columnas):
                mat[i].append(0)
        cab = self.mat
        p = self.primerNodo()
        while p != cab:
            q = p.retorna_liga_derecha()
            while q != p:
                t = q.retorna_dato()
                f = t.get_fila()
                c = t.get_col()
                v = t.get_value()
                mat[f - 1][c - 1] = v
                q = q.retorna_liga_derecha()
            t = p.retorna_dato()
            p = t.get_value()
        return mat



