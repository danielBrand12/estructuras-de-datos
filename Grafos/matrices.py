class Tripleta():
    """Método constructor"""
    def __init__(self, fila, col, value):
        self.fila = fila
        self.col = col
        self.value = value

    """Métodos getters & setters"""
    def set_fila(self, fila):
        self.fila = fila

    def set_col(self, col):
        self.col = col

    def set_value(self, value):
        self.value = value

    def get_fila(self):
        return self.fila

    def get_col(self):
        return self.col

    def get_value(self):
        return self.value

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

class MatEnTripletas():

    """Constructor dónde definimos una lista donde
        guardaremos las tripletas"""
    def __init__(self, fila, col, value):
        self.filas = fila
        self.columnas = col
        self.lista = []
        tripleta = Tripleta(fila, col, value)
        self.lista.append(tripleta)

    def cant(self):
        return len(self.lista)

    def numero_filas(self):
        return self.lista[0].get_fila()

    def numero_col(self):
        return self.lista[0].get_col()

    def numero_values(self):
        return self.lista[0].get_value()

    def asigna_tripleta(self, tripleta, k):
        if (len(self.lista) - 1 < k):
            for i in range(len(self.lista) - 1, k):
                self.lista.append(None)
        self.lista[k] = tripleta

    def retorna_num_tripleta(self):
        return self.lista[0].get_value()

    def retorna_tripleta(self, k):
        return self.lista[k]

    def asigna_numero_tripletas(self, k):
        self.lista[0].set_value(k)

    def muestra_matriz(self):
        aux = self.lista
        for i in range(1, len(self.lista)):
            print(aux[i].get_fila(), aux[i].get_col(), aux[i].get_value())

    def inserta_tripleta(self, tripleta):
        tx = self.retorna_tripleta(0)
        p = tx.get_value()
        i = 0
        t = self.retorna_tripleta(i)
        if(tripleta.get_fila() > tx.get_fila() or tripleta.get_col() > tx.get_col()):
            print("No puede modificar las dimensiones de la matriz")
            return
        while(i <= p and t.get_fila() < tripleta.get_fila()):
            i += 1
            t = self.retorna_tripleta(i)
        while (i <= p and t.get_fila() == tripleta.get_fila()
        and t.get_col() < tripleta.get_col()):
            i += 1
            try:
                t = self.retorna_tripleta(i)
            except:
                pass
        p = p + 1
        """j = p - 1"""
        self.lista.insert(i, tripleta)
        """while(j >= i):
            self.lista[j + 1] = self.lista[j]
            j = j - 1
        self.lista[i] = tripleta"""
        self.asigna_numero_tripletas(p)

    def agrega_tripleta(self, tripleta):
        tx = self.retorna_tripleta(0)
        if (tripleta.get_fila() > tx.get_fila() or tripleta.get_col() > tx.get_col()):
            print("No puede modificar las dimensiones de la matriz")
            return
        p = self.retorna_tripleta(0).get_value()
        p = p + 1
        self.asigna_numero_tripletas(p)
        self.lista.append(tripleta)

    def suma(self, matriz):
        ma = self.numero_filas()
        na = self.numero_col()
        mb = matriz.numero_filas()
        nb = matriz.numero_col()
        p = self.retorna_num_tripleta()
        q = matriz.retorna_num_tripleta()
        if ((ma != mb) or (na != nb)):
            print("Matrices de diferentes dimensiones no se pueden sumar")
            return None
        c = MatEnTripletas(ma, na, 0)
        i = 1
        j = 1
        k = 0
        while((i <= p) and (j <= q)):
            ti = self.retorna_tripleta(i)
            tj = matriz.retorna_tripleta(j)
            fi = ti.get_fila()
            fj = tj.get_fila()
            k = k + 1
            aux = self.comparar(fi, fj)
            if(aux == -1):
                c.asigna_tripleta(ti, k)
                i = i + 1
            elif(aux == 1):
                c.asigna_tripleta(tj, k)
                j = j + 1
            elif(aux == 0):
                ci = ti.get_col()
                cj = tj.get_col()
                aux2 = self.comparar(ci, cj)
                if(aux2 == -1):
                    c.asigna_tripleta(ti, k)
                    i = i + 1
                elif(aux2 == 1):
                    c.asigna_tripleta(tj, k)
                    j = j + 1
                elif(aux2 == 0):
                    vi = ti.get_value()
                    vj = tj.get_value()
                    ss = vi + vj
                    if (ss != 0):
                        tx = Tripleta(fi, ci, ss)
                        c.asigna_tripleta(tx, k)
                    else:
                        k = k - 1
                    i = i + 1
                    j = j + 1
        while(i <= p):
            ti = self.retorna_tripleta(i)
            k = k + 1
            c.asigna_tripleta(ti, k)
            i = i + 1
        while(j <= q):
            tj = matriz.retorna_tripleta(j)
            k = k + 1
            c.asigna_tripleta(tj, k)
            j = j + 1
        c.asigna_numero_tripletas(k)
        return c

    def comparar(self, a, b):
        if(a < b):
            return -1
        if(a == b):
            return 0
        return 1

    def transpuesta(self):
        p = self.retorna_num_tripleta()
        b = MatEnTripletas(self.numero_col(), self.numero_filas(), 0)
        i = 1
        while(i <= p):
            ti = self.retorna_tripleta(i)
            f = ti.get_col()
            c = ti.get_fila()
            v = ti.get_value()
            ti = Tripleta(f, c, v)
            b.lista.append(ti)
            i = i + 1
        b.asigna_numero_tripletas(p)
        return b

    def intercambia_filas(self, i, j):
        if(i == j): return
        if(i > j):
            k = i
            i = j
            j = k
        s = self.vector_limites()
        mi = s[i]
        ni = s[i + 1] - s[i]
        mj = s[j]
        nj = s[j + 1] - s[j]
        ki = 1
        kj = 1
        while(ki <= ni and kj <= nj):
            ci = self.lista[mi].get_col()
            cj = self.lista[mj].get_col()
            vi = self.lista[mi].get_value()
            vj = self.lista[mj].get_value()
            self.lista[mi].set_col(cj)
            self.lista[mi].set_value(vj)
            self.lista[mj].set_col(ci)
            self.lista[mj].set_value(vi)
            ki = ki + 1
            kj = kj + 1
            mj = mj + 1
            mi = mi + 1
            if(kj <= nj):
                pp = mj - 1
                aux = MatEnTripletas(self.numero_filas(), self.numero_col(), 0)
                while(kj <= nj):
                    t = Tripleta(i, self.numero_col(), self.lista[mj].get_value())
                    aux.inserta_tripleta(t)
                    kj = kj + 1
                    mj = mj + 1
                mj = mj - 1
                while(pp >= mi):
                    self.lista[mj] = self.lista[pp]
                    mj = mj - 1
                    pp = pp - 1
                for k in range(1, aux.retorna_num_tripleta()):
                    self.lista[mi] = aux.retorna_tripleta(k)
                    mi = mi + 1
                return
            if(ki <= ni):
                pp = mi
                t = Tripleta(self.numero_filas(), self.numero_col(), 0)
                aux = MatEnTripletas(self.numero_filas(), self.numero_col(), 0)
                while(ki <= ni):
                    t = Tripleta(j, self.lista[mi].numero_col(),self.lista[mi].get_value())
                    aux.inserta_tripleta(t)
                    ki = ki + 1
                    mi = mi + 1
                while(mi < mj):
                    self.lista[pp] = self.lista[mi]
                    mi = mi + 1
                    pp = pp + 1
                for k in range(1, aux.retorna_num_tripleta()):
                    self.lista[pp] = aux.retorna_tripleta(k)
                    pp = pp + 1

    def vector_limites(self):
        p = self.retorna_num_tripleta()
        n = self.numero_filas()
        s = []
        for k in range(1, n):
            s[k] = 0
        for k in range(1, p):
            tx = self.retorna_tripleta(k)
            s[tx.get_fila()] = s[tx.get_fila()] + 1
        s[n + 1] = p + 1
        for k in reversed(range(1, n)):
            s[k] = s[k + 1] - s[k]

    def multiplica(self, b):
        m = self.numero_filas()
        n = self.numero_col()
        na = self.retorna_num_tripleta()
        if(n != b.numero_filas()):
            print("No se pueden multiplicar las matrices")
            return None
        p = b.numero_col()
        nb = b.retorna_num_tripleta()
        tx = Tripleta(m + 1, 0, 0)
        self.asigna_tripleta(tx, na + 1)
        c = MatEnTripletas(m, p, 0)
        bt = b.transpuesta()
        tx = Tripleta(p + 1, 0, 0)
        bt.asigna_tripleta(tx, nb + 1)
        i = 1
        ti = self.retorna_tripleta(i)
        fila_actual = ti.get_fila()
        inicio_final_actual = i
        k = 0
        suma = 0
        while(i <= na):
            j = 1
            tj = bt.retorna_tripleta(j)
            col_actual = tj.get_col()
            while(j <= nb + 1):
                tj = bt.retorna_tripleta(j)
                if(ti.get_fila() != fila_actual):
                    if(suma != 0):
                       k = k + 1
                       c.asigna_numero_tripletas(k)
                       tx = Tripleta(fila_actual,col_actual,suma)
                       c.asigna_tripleta(tx, k)
                       suma = 0
                    while(tj.get_fila() == col_actual):
                        j = j + 1
                        tj = bt.retorna_tripleta(j)
                    col_actual = tj.get_fila()
                    i = inicio_final_actual
                    ti = self.retorna_tripleta(i)
                    continue
                if(tj.get_fila() != col_actual):
                    if(suma != 0):
                        k = k + 1
                        c.asigna_numero_tripletas(k)
                        tx = Tripleta(fila_actual,col_actual,suma)
                        c.asigna_tripleta(tx, k)
                        suma = 0
                    col_actual = tj.get_fila()
                    i = inicio_final_actual
                    ti = self.retorna_tripleta(i)
                    continue
                if(ti.get_col() < tj.get_col()):
                    i = i + 1
                    ti = self.retorna_tripleta(i)
                    continue
                if(ti.get_col() == tj.get_col()):
                    sti = ti.get_value()
                    stj = tj.get_value()
                    suma = suma + sti*stj
                    i += 1
                    j += 1
                    ti = self.retorna_tripleta(i)
                    continue
                j = j + 1
            while(ti.get_fila() == fila_actual):
                i = i + 1
                ti = self.retorna_tripleta(i)
            inicio_final_actual = i
            fila_actual = ti.get_fila()
        return c

    def aCuadricula(self):
        mat = []
        for i in range(self.filas):
            mat.append([])
            for j in range(self.columnas):
                mat[i].append(0)
        aux = self.lista
        for i in range(1, len(self.lista)):
            mat[aux[i].get_fila() - 1][aux[i].get_col() - 1] = aux[i].get_value()
        return mat

class MatrizForma1:

    def __init__(self, m, n):
        self.filas = m
        self.columnas = n
        t = Tripleta(m, n, None)
        self.mat = NodoDoble(t)
        t.set_value(self.mat)
        self.mat.asigna_dato(t)

    def fin_de_recorrido(self, p):
        return p == self.mat

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
            t = Tripleta(i, i, self.mat)
            x = NodoDoble(t)
            x.asigna_liga_derecha(x)
            x.asigna_liga_izquierda(x)
            t = ultimo.retorna_dato()
            t.set_value(x)
            ultimo.asigna_dato(t)
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