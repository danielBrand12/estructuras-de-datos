# Grafo como lista ligada de adyacencia
import numpy as np
import GrafoMA as MA


class NodoSimple:
    def __init__(self, d):
        self.dato = d
        self.liga = None

    def retorna_dato(self):
        return self.dato

    def asigna_dato(self, d):
        self.dato = d

    def asigna_liga(self, x):
        self.liga = x

    def retorna_liga(self):
        return self.liga


class GrafoListaAdyacencia:
    def __init__(self, vertices):
        self.tamaño = vertices
        self.vector = np.full(vertices + 1, None)
        self.visitado = np.zeros((vertices + 1))
        self.cola = []

    def conectar_nodos(self, nodo1, nodo2):
        x = NodoSimple(nodo2)
        x.asigna_liga(self.vector[nodo1])
        self.vector[nodo1] = x

    def LLA_a_MFD(self):  # lista ligada de adyacencia a matriz dispiersa en tripletas
        matriz_MA = MA.GrafoMatrizAdyacencia(self.tamaño)
        for i in range(self.tamaño):
            p = self.vector[i]
            while p is not None:
                q = p.retorna_dato()
                matriz_MA.conectar_adyacencia(i, q)
                p = p.retorna_liga()
        return matriz_MA

    def dfs(self, v):
        print(v)
        self.visitado[v] = 1
        p = self.vector[v]
        while p is not None:
            w = p.retorna_dato()
            if self.visitado[w] == 0:
                self.dfs(w)
            p = p.retorna_liga()

    def bfs(self):
        self.mostrar_bfs(0)

    def mostrar_bfs(self, v):
        self.visitado[v] = 1
        self.cola.append(v)
        while not len(self.cola) == 0:
            v = self.cola.pop(0)
            print(v)
            p = self.vector[v]
            while p is not None:
                i = p.retorna_dato()
                if self.visitado[i] == 0:
                    self.visitado[i] = 1
                    self.cola.append(i)
                p = p.retorna_liga()