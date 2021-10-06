class NodoLg:
    def __init__(self):
        self.dato = None
        self.swich = None       #si sw es 0 entonces el el campo será un dato, si es 1 el campo será un apuntador a otra lg
        self.liga = None

    def asigna_dato(self, d):
        self.dato = d

    def retorna_dato(self):
        return self.dato

    def asigna_sw(self, sw):
        self.swich = sw

    def retorna_sw(self):
        return self.swich

    def asigna_liga(self, x):
        self.liga = x

    def retorna_liga(self):
        return self.liga


class ListaGeneralizada:

    def __init__(self):
        self.tamaño = 0
        self.primero = None
        self.ultimo = None

    def construye_lg(self, s):
        n = len(s)
        pila = []
        self.primero = NodoLg()
        self.ultimo = self.primero
        for i in range(n):
            if(s[i] == "("):
                pila.append(self.ultimo)
                self.ultimo.asigna_sw(1)
                x = NodoLg()
                self.ultimo.asigna_dato(x)
                self.ultimo = x
                self.tamaño = self.tamaño + 1
            elif(s[i] == ","):
                x = NodoLg()
                self.ultimo.asigna_liga(x)
                self.ultimo = x
            elif(s[i] == ")"):
                self.ultimo = pila.pop()
            else:
                self.ultimo.asigna_sw(0)
                self.ultimo.asigna_dato(s[i])
                self.tamaño = self.tamaño + 1

    def construye_arbol(self, s):
        n = len(s)
        pila = []
        self.primero = NodoLg()
        self.ultimo = self.primero
        for i in range(n):
            if (s[i] == "("):
                pila.append(self.ultimo)
                self.ultimo.asigna_sw(1)
                x = NodoLg()
                self.ultimo.asigna_dato(x)
                self.ultimo = x
                self.tamaño = self.tamaño + 1
            elif (s[i] == ","):
                x = NodoLg()
                self.ultimo.asigna_liga(x)
                self.ultimo = x
            elif (s[i] == ")"):
                self.ultimo = pila.pop()
            else:
                self.ultimo.asigna_sw(0)
                self.ultimo.asigna_dato(s[i])
                self.tamaño = self.tamaño + 1
                if(s[i+1] == "("):
                    x = NodoLg()
                    self.ultimo.asigna_liga(x)
                    self.ultimo = x

    def muestra_arbol(self, r):
        while(True):
            if r.retorna_sw() == 0 and r.retorna_liga() == None:
                break
            if r.retorna_sw == 1:
                self.muestra_arbol(r.retorna_dato())
                r = r.retorna_liga()
            else:
                print(r.retorna_dato())
                r = r.retorna_liga()

    def construye_hilera(self, p):
        s = ""
        ultimo = p
        if(ultimo.retorna_sw() == 0 and ultimo.retorna_liga() == None):
            s = s + ultimo.retorna_dato() + ")"
            return s
        elif(ultimo.retorna_sw() == 1):
            s = s + "("
            a = self.construye_hilera(ultimo.retorna_dato())
            s = s + a
            ultimo = ultimo.retorna_liga()
            if(ultimo != None):
                b = self.construye_hilera(ultimo)
                s = s + "," + b
        else:
            a = ultimo.retorna_dato()
            s = s + a + ","
            if(ultimo.retorna_liga() != None):
                s = s + self.construye_hilera(ultimo.retorna_liga())
        s = s + ")"
        return s

    def hojas(self, r):
        if(r == None): return 0
        if(r.retorna_sw() == 1):
            p = r.retorna_dato()
            p = p.retorna_liga()
        else: p = r.retorna_liga()
        if(p == None): return 1
        n = 0
        while(p != None):
            if(p.retorna_sw() == 0):
                n = n + 1
            else:
                n = n + self.hojas(p.retorna_dato())
            p = p.retorna_liga()
        return n

    def grado(self, r):
        if(r == None): return 0
        if (r.retorna_sw() == 1):
            p = r.retorna_dato()
            p = p.retorna_liga()
        else:
            p = r.retorna_liga()
        if(p == None): return 0
        n = 0
        mayor = 0
        while(p != None):
            n = n + 1
            if(p.retorna_sw() == 1):
                g = self.grado(p.retorna_dato())
                if(g > mayor): mayor = g
            p = p.retorna_liga()
        if(n > mayor): return n
        return mayor

    def insertar(self, x, origen=None):
        if (origen == None):
            p = self.primero
        else:
            p = origen
        ant = p
        while (p.retorna_dato() < x.retorna_dato() and p != None):
            ant = p
            p = p.retorna_liga()
            if (p.retorna_sw() == 1):
                ant = p
                p = p.retorna_liga()
        if (ant.retorna_sw() == 1):
            self.insertar(x, ant)
        else:
            ant.asigna_liga(x)
            x.asigna_liga(p)
            if (p == None):
                self.ultimo = x
        return

    def insertList(self, listLg, origen=None):
        if (origen == None):
            p = self.primero
        else:
            p = origen
        ant = p
        q = listLg.primero
        q2 = listLg.ultimo
        while (p.retona_dato() > q.retornaDato and p.retorna_dato() < q2.retorna_dato() and p != None):
            ant = p
            p = p.retorna_liga()
            if (p.retorna_sw() == 1):
                ant = p
                p = p.retorna_liga()
        if (ant.retorna_sw == 1):
            self.insertList(listLg, ant)
        else:
            aux = NodoLg(None, 1)
            aux.asigna_dato(q)
            ant.asigna_liga(aux)
            aux.asigna_liga(p)
        return

    def borrar(self, dato, origen=None):
        p = NodoLg()
        if (origen == None):
            p = self.primero
        else:
            p = origen
        ant = p
        while (p.retorna_dato() < dato and p != None):
            ant = p
            p = p.retorna_liga()
            if (p.retona_sw() == 1):
                ant = p
                p = p.retona_liga()
        if (ant.retorna_sw() == 1 and p.retona_dato() != dato):
            self.borrar(dato, ant)
            return
        if (p.retorna_dato() == dato):
            ant.asigna_liga(p.retona_liga())
        return


a = "(a(b,c,e))"
lista = ListaGeneralizada()
lista.construye_arbol(a)
lista.muestra_arbol(lista.primero)


