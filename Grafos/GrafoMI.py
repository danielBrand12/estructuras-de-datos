import numpy as np
import matrices as mat
import GrafoLLA as LLA
import GrafoMLA as MLA
import GrafoMA as MA


class matriz_incidencia:

    def __init__(self, vertices, aristas):
        self.cant_nodos = vertices
        self.cant_aristas = aristas
        self.MI = np.zeros((vertices, aristas))
        self.inciFD = mat.MatEnTripletas(vertices, aristas, 0)
        self.inciF1 = mat.MatrizForma1(vertices, aristas)
        self.visitado = np.zeros((vertices + 1))
        self.cola = []

    def conectar(self, nodo1, nodo2, arista):
        self.MI[nodo1][arista] = 1
        self.MI[nodo2][arista] = 1

    def conectar_FD(self, nodo1, nodo2, arista):
        t1 = mat.Tripleta(nodo1, arista, 1)
        t2 = mat.Tripleta(nodo2, arista, 1)
        self.inciFD.agrega_tripleta(t1)
        self.inciFD.agrega_tripleta(t2)

    def conectar_F1(self, nodo1, nodo2, arista):
        t1 = mat.Tripleta(nodo1, arista, 1)
        n1 = mat.NodoDoble(t1)
        self.inciF1.conectaPorFilas(n1)
        self.inciF1.conectaPorColumnas(n1)

        t2 = mat.Tripleta(nodo2, arista, 1)
        n2 = mat.NodoDoble(t2)
        self.inciF1.conectaPorFilas(n2)
        self.inciF1.conectaPorColumnas(n2)

    def MI_a_LLA(self):
        matriz_LLA = LLA.GrafoListaAdyacencia(self.cant_nodos)
        for i in range(self.cant_aristas):
            aux = []
            for j in range(self.cant_nodos):
                if self.MI[j][i] == 1:
                    aux.append(j)
            matriz_LLA.conectar_nodos(aux[0], aux[1])
        return matriz_LLA

    def MI_a_MLA(self):
        matriz_MLA = MLA.grafoMLA(self.cant_nodos)
        for i in range(self.cant_aristas):
            aux = []
            for j in range(self.cant_nodos):
                if self.MI[j][i] == 1:
                    aux.append(j)
            matriz_MLA.conectar_nodos(aux[0], aux[1])
        return matriz_MLA

    def MI_a_MA(self):
        matriz_MA = MA.GrafoMatrizAdyacencia(self.cant_nodos)
        for i in range(self.cant_aristas):
            aux = []
            for j in range(self.cant_nodos):
                if self.MI[j][i] == 1:
                    aux.append(j)
            matriz_MA.conectar_adyacencia(aux[0], aux[1])
            matriz_MA.conectar_adyacencia(aux[1], aux[0])
        return matriz_MA

    def MIFD_a_MA(self):
        matriz_MA = MA.GrafoMatrizAdyacencia(self.cant_nodos)
        for i in range(self.inciFD.cant()):
            for j in range(i, self.inciFD.cant()):
                x = self.inciFD.retorna_tripleta(i).get_col()
                y = self.inciFD.retorna_tripleta(j).get_col()
                if x == y:
                    a = self.inciFD.retorna_tripleta(i).get_fila()
                    b = self.inciFD.retorna_tripleta(j).get_fila()
                    matriz_MA.conectar_adyacencia(a, b)
                    break
        return matriz_MA

    def dfs(self):
        self.mostrar_dfs()

    def mostrar_dfs(self, v):
        print(v)
        self.visitado[v] = 1
        for i in range(self.cant_aristas):
            if self.MI[v][i] == 1:
                for j in range(self.cant_nodos):
                    if self.MI[j][i] == 1 and j is not v and self.visitado[j] == 0:
                        self.mostrar_dfs(i)

