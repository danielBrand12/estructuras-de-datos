from tripleta import Tripleta

class MatEnTripletas():

    """Constructor dónde definimos una lista donde
        guardaremos las tripletas"""
    def __init__(self, fila, col, value):
        self.filas = fila
        self.columnas = col
        self.lista = []
        tripleta = Tripleta(fila, col, value)
        self.lista.append(tripleta)

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








