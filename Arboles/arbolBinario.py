class NodoAVL:
    def __init__(self, d):
        self.liga_izq = self.liga_der = None
        self.dato = d
        self.fb = 0

    def asigna_LI(self, x):
        self.liga_izq = x

    def asigna_LD(self, x):
        self.liga_der = x

    def asigna_dato(self, d):
        self.dato = d

    def retorna_dato(self):
        return self.dato

    def retorna_LI(self):
        return self.liga_izq

    def retorna_LD(self):
        return self.liga_der

    def grado(self):
        p = 0
        if(self.liga_der != None): p = p + 1
        if(self.liga_izq != None): p = p + 1
        return p

    def asigna_FB(self, fb):
        self.fb = fb

    def retorna_FB(self):
        return self.fb

import string
import random
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return (self.raiz == None)

    def agregar(self, d):
        n = NodoAVL(d)
        if(self.es_vacio()):
            self.raiz = n
            return
        p = self.raiz
        q = None
        while(p != None):
            if(p.retorna_dato == d):
                return
            q = p
            if(d < p.retorna_dato()):
                p = p.retorna_LI()
            else:
                p = p.retorna_LD()
        if(d > q.retorna_dato()):
            q.asigna_LD(n)
        else:
            q.asigna_LI(n)

    def inorden(self, x):
        if(x != None):
            self.inorden(x.retorna_LI())
            print(x.retorna_dato())
            self.inorden(x.retorna_LD())

    def preorden(self, x):
        if(x != None):
            print(x.retorna_dato())
            self.preorden(x.retorna_LI())
            self.preorden(x.retorna_LD())

    def posorden(self, x):
        if(x != None):
            self.posorden(x.retorna_LI())
            self.posorden(x.retorna_LD())
            print(x.retorna_dato())

    def hojas(self):
        if(self.es_vacio()): return 0
        return(self.hojas_recursivo(self.raiz))

    def hojas_recursivo(self, x):
        if (x == None): return 0
        if (x.retorna_LI == None and x.retorna_LD() == None): return 1
        izquierda = self.hojas_recursivo(x.retorna_LI())
        derecha = self.hojas_recursivo(x.retorna_LD())
        return (izquierda + derecha)

    def grado(self):
        if(self.es_vacio()): return 0
        return grado_recursivo(self.raiz)

    def grado_recursivo(self, x):
        if(x == None): return 0
        p = x.grado()
        pmax = p
        p = grado_recursivo(x.retorna_LD())
        if(p > pmax): pmax = p
        p = grado_recursivo(x.retorna_LI())
        if(p > pmax): pmax = p
        if(pmax == 2): return 2
        return pmax

    def altura(self):
        return self.altura_recursiva(self.raiz)

    def altura_recursiva(self, x):
        if(x == None): return 0
        izquierda = self.altura_recursiva(x.retorna_LI())
        derecha = self.altura_recursiva(x.retorna_LD())
        if(izquierda > derecha): return izquierda+1
        return derecha+1

    def padre(self, r, dato):
        padre = None
        d = None
        if r != None:
            if r.retorna_LI() != None:
                p = r.retorna_LI()
                d = p.retorna_dato()
                if d == dato:
                    padre = r.retorna_dato()
            if padre == None:
                if r.retorna_LD() != None:
                    p = r.retorna_LD()
                    d = p.retorna_dato()
                    if d == dato:
                        padre = r.retorna_dato()
            if padre == None:
                padre = self.padre(r.retorna_LI(), dato)
            if padre == None:
                padre = self.padre(r.retorna_LD(), dato)
        return padre

    def retorna_nodo(self, r, dato):
        if self.raiz.retorna_dato() == dato:
            return self.raiz
        nodo = None
        d = None
        if r != None:
            if r.retorna_LI() != None:
                p = r.retorna_LI()
                d = p.retorna_dato()
                if d == dato:
                    nodo = p
                    return nodo
            if nodo == None:
                if r.retorna_LD() != None:
                    p = r.retorna_LD()
                    d = p.retorna_dato()
                    if d == dato:
                        nodo = p
                        return nodo
            if nodo == None:
                nodo = self.retorna_nodo(r.retorna_LI(), dato)
            if nodo == None:
                nodo = self.retorna_nodo(r.retorna_LD(), dato)
        return nodo

    def llenar_aleatorio(self, tamaño):
        lista = []
        for i in range(tamaño):
            letra = random.SystemRandom().choice(string.ascii_letters)
            letra = letra.lower()
            if letra in lista:
                while True:
                    letra = random.SystemRandom().choice(string.ascii_letters)
                    letra = letra.lower()
                    if not letra in lista: break
            lista.append(letra)
            self.agregar(letra)

    def llenar_manual(self, inorden, preorden):
        x = NodoAVL(preorden[0])
        if self.raiz == None: self.raiz = x
        if len(preorden) == 1: return x
        k = 0
        while preorden[0] != inorden[k]:
            k = k + 1
        apre = preorden[1:k+1]
        ain = inorden[0:k]
        x.asigna_LI(self.llenar_manual(ain,apre))
        apre = preorden[k+1:len(preorden)]
        ain = inorden[k+1:len(inorden)]
        x.asigna_LD(self.llenar_manual(ain, apre))
        return x

    def numero_hijos(self, nodo):
        vertice = self.retorna_nodo(self.raiz, nodo)
        hijo1 = vertice.retorna_LI()
        hijo2 = vertice.retorna_LD()
        cont = 0
        if hijo1 != None:
            cont += 1
        if hijo2 != None:
            cont += 1
        return cont

    def hermano(self, nodo):
        if self.raiz.retorna_dato() == nodo:
            return None
        pa = self.padre(self.raiz, nodo)
        nodo_pa = self.retorna_nodo(self.raiz, pa)
        izq = nodo_pa.retorna_LI()
        der = nodo_pa.retorna_LD()
        if izq and der != None and izq.retorna_dato() == nodo:
            return der.retorna_dato()
        if der and izq  != None and der.retorna_dato() == nodo:
            return izq.retorna_dato()
        return None

    def es_izquierdo(self, nodo):
        if self.raiz.retorna_dato() == nodo:
            return None
        padre = self.padre(self.raiz, nodo)
        nodo_padre = self.retorna_nodo(self.raiz, padre)
        hijo_izq = nodo_padre.retorna_LI()
        hijo_der = nodo_padre.retorna_LD()
        if hijo_izq != None and hijo_izq.retorna_dato() == nodo:
            return True
        elif hijo_der != None and hijo_der.retorna_dato() == nodo:
            return False

    def tio(self, nodo):
        if self.raiz.retorna_dato() == nodo:
            return None
        pa = self.padre(self.raiz, nodo)
        if self.raiz.retorna_dato() == pa:
            return None
        ab = self.abuelo(nodo)
        nodo_ab = self.retorna_nodo(self.raiz, ab)
        izq = nodo_ab.retorna_LI()
        der = nodo_ab.retorna_LD()
        if izq and der != None and izq.retorna_dato() == pa:
            return der.retorna_dato()
        if der and izq != None and der.retorna_dato() == pa:
            return izq.retorna_dato()
        return None

    def abuelo(self, nodo):
        if self.raiz.retorna_dato() == nodo:
            return None
        padre = self.padre(self.raiz, nodo)
        if padre == self.raiz.retorna_dato():
            return None
        abuelo = self.padre(self.raiz, padre)
        return abuelo

    def ancestros(self, nodo):
        pila = []
        p = nodo
        while (p != self.raiz.retorna_dato()):
            p = self.padre(self.raiz, p)
            pila.append(p)
        return pila

class ArbolAVL:
    def __init__(self):
        self.raiz = NodoAVL(None)

    def es_vacio(self):
        return self.raiz.retorna_dato() == None

    def agregar(self,d):
        n = NodoAVL(d)
        if(self.es_vacio()):
            self.raiz = n
            return
        p = self.raiz
        q = NodoAVL(None)
        pp = q
        pivote = p
        while(p != None):
            if(p.retorna_dato() == d):
                print("El dato ya existe")
                return
            if(p.retornaGB != 0):
                pivote = p
                pp = q
            q = p
            if(d < p.retorna_dato()):
                p = p.retorna_LI()
            else:
                p = p.retorna_LD()

        if(d > q.retorna_dato()):
            q.asigna_LD(n)
        else:
            q.asigna_LI(n)

        aux = pivote.retorna_FB()
        if(d > pivote.retorna_dato()):
            pivote.asigna_FB(aux - 1)
            q = pivote.retorna_LD()
        else:
            pivote.asigna_FB(aux + 1)
            q = pivote.retorna_LI()
        p = q

        while(p != n):
            if(d < p.retorna_dato()):
                p.asigna_FB(1)
                p = p.retorna_LI()
            else:
                p.asigna_FB(-1)
                p = p.retorna_LD()

        if(abs(pivote.retorna_FB()) < 2):
            return

        if(pivote.retorna_FB() == 2):
            if(q.retorna_FB == 1):
                q = una_rotacion_a_la_derecha(pivote, q)
            else:
                q = doble_rotacion_a_la_derecha(pivote, q)
        else:
            if(q.retorna_FB() == 1):
                q = doble_rotacion_a_la_izquierda(pivote, q)
            else:
                q = una_rotacion_a_la_izquierda(pivote, q)

        if(pp == None):
            self.raiz = q
            return
        if(pivote == pp.retorna_LI()):
            pp.asigna_LI(q)
        else:
            pp.asigna_LD(q)

    def una_rotacion_a_la_derecha(self,p, q):
        p.asigna_LI(q.retorna_LD())
        q.asigna_LD(p)
        p.asigna_FB(0)
        q.asigna_FB(0)
        return q

    def una_rotacion_a_la_izquierda(self, p, q):
        p.asigna_LD(q.retorna_LI())
        q.asigna_LI(p)
        p.asigna_FB(0)
        q.asigna_FB(0)
        return q

    def doble_rotacion_a_la_derecha(self, p , q):
        r = q.retorna_LD()
        q.asigna_LD(p.retorna_LI())
        r.asigna_LI(q)
        p.asigna_LI(r.retorna_LD())
        r.asigna_LD(p)
        aux = r.retorna_FB()
        if aux == -1:
            p.asigna_FB(0)
            q.asigna_FB(1)
        elif aux == 0:
            p.asigna_FB(0)
            q.asigna_FB(0)
        elif aux == 1:
            p.asigna_FB(-1)
            q.asigna_FB(0)
        r.asigna_FB(0)
        return r

    def doble_rotacion_a_la_derecha(self, p , q):
        r = q.retorna_LI()
        q.asigna_LI(p.retorna_LD())
        r.asigna_LD(q)
        p.asigna_LD(r.retorna_LI())
        r.asigna_LI(p)
        aux = r.retorna_FB()
        if aux == -1:
            p.asigna_FB(1)
            q.asigna_FB(0)
        elif aux == 0:
            p.asigna_FB(0)
            q.asigna_FB(0)
        elif aux == 1:
            p.asigna_FB(0)
            q.asigna_FB(-1)
       # r.asigna_FB(0)
        return r