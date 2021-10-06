import numpy as np
import matrices as mat
import GrafoLLA as LLA
import GrafoMLA as MLA
import GrafoMI as MI
import Conjuntos as CO


class GrafoMatrizAdyacencia:

    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.adyaFD = mat.MatEnTripletas(tamaño, tamaño, 0)
        self.adyaF1 = mat.MatrizForma1(tamaño, tamaño)
        self.adyaF1.construyeNodosCabeza()
        self.adyaF2 = mat.MatrizForma2(tamaño, tamaño)
        self.adyacencia = np.zeros((tamaño + 1, tamaño + 1))
        self.visitado = np.zeros((tamaño + 1))
        self.cola = []
        self.lados = CO.conjunto()
        self.costos = np.zeros((tamaño + 1, tamaño + 1))

    def conectar_adyacencia(self, nodo1, nodo2):
        if nodo1 > self.tamaño or nodo2 > self.tamaño:
            print("No se puede conectar el par de nodos. ")
            return
        self.adyacencia[nodo1][nodo2] = 1

    def conectar_adyacecia_costos(self, nodo1, nodo2, costo):
        self.costos[nodo1][nodo2] = costo

    def conectar_en_tripletas(self, nodo1, nodo2):
        if nodo1 > self.tamaño or nodo2 > self.tamaño:
            print("No se puede conectar el par de nodos. ")
            return
        t = mat.Tripleta(nodo1, nodo2, 1)
        self.adyaFD.agrega_tripleta(t)

    def conecta_en_tripletas_F1(self, nodo1, nodo2):
        if nodo1 > self.tamaño or nodo2 > self.tamaño:
            print("No se puede conectar el par de nodos. ")
            return
        t = mat.Tripleta(nodo1, nodo2, 1)
        n = mat.NodoDoble(t)
        self.adyaF1.conectaPorFilas(n)
        self.adyaF1.conectaPorColumnas(n)

    def conecta_en_tripletas_F2(self, nodo1, nodo2):
        if nodo1 > self.tamaño or nodo2 > self.tamaño:
            print("No se puede conectar el par de nodos. ")
            return
        t = mat.Tripleta(nodo1, nodo2, 1)
        n = mat.NodoDoble(t)
        self.adyaF2.conectaPorFilasForma2(n)
        self.adyaF2.conectaPorColumna2(n)

    def de_MA_a_LLA(self):
        matriz_LLA = LLA.GrafoListaAdyacencia(self.tamaño)
        for i in range(0, self.tamaño + 1):
            for j in range(i, self.tamaño + 1):
                if self.adyacencia[i][j] == 1:
                    matriz_LLA.conectar_nodos(i, j)
        return matriz_LLA

    def de_FD_a_LLA(self):
        if self.adyaFD.numero_values() == 0:
            print("Grafo vacío")
            return
        matriz_LLA = LLA.GrafoListaAdyacencia(self.tamaño)
        for i in range(1, self.adyaFD.numero_values() + 1):
            t = self.adyaFD.retorna_tripleta(i)
            nodo1 = t.get_fila()
            nodo2 = t.get_col()
            matriz_LLA.conectar_nodos(nodo1, nodo2)
        return matriz_LLA

    def de_F1_a_LLA(self):
        matriz_LLA = LLA.GrafoListaAdyacencia(self.tamaño)
        p = self.adyaF1.primerNodo()
        while not self.adyaF1.fin_de_recorrido(p):
            q = p.retorna_liga_derecha()
            while q != p:
                t = q.retorna_dato()
                m = t.get_fila()
                n = t.get_col()
                matriz_LLA.conectar_nodos(m, n)
                q = q.retorna_liga_derecha()
            t = p.get_value()
            p = t.retorna_dato()
        return matriz_LLA

    def de_F2_a_LLA(self):
        matriz_LLA = LLA.GrafoListaAdyacencia(self.tamaño)
        p = self.adyaF2.nodoCabeza()
        while not self.adyaF2.finDeRecorrido(p):
            t = p.retorna_dato()
            m = t.get_fila()
            n = t.get_col()
            matriz_LLA.conectar_nodos(m, n)
            p = p.retorna_liga_derecha()

    def de_MA_a_MLA(self):
        matriz_MLA = MLA.grafoMLA(self.tamaño)
        for i in range(self.tamaño + 1):
            for j in range(i, self.tamaño + 1):
                if self.adyacencia[i][j] == 1:
                    matriz_MLA.conectar_nodos(i, j)
        return matriz_MLA

    def de_MA_a_MI(self):
        k = self.numero_aristas()
        incidencia = MI.matriz_incidencia(self.tamaño + 1, k)
        k = 0
        for i in range(self.tamaño + 1):
            for j in range(i, self.tamaño + 1):
                if self.adyacencia[i][j] == 1:
                    incidencia.conectar(i, j, k)
                    k = k + 1

    def numero_aristas(self):
        k = 0
        for i in range(self.tamaño + 1):
            for j in range(i, self.tamaño + 1):
                if self.adyacencia[i][j] == 1:
                    k = k + 1
        return k

    def bfs(self, v):
        self.visitado[v] = 1
        self.cola.append(v)
        while len(self.cola) is not 0:
            v = self.cola.pop(0)
            print(v)
            for w in range(self.tamaño):
                if self.adyacencia[v][w] == 1:
                    if self.visitado[w] == 0:
                        self.visitado[w] = 1
                        self.cola.append(w)

    def dfs(self):
        self.dfs_recursivo(0, 0)

    def dfs_recursivo(self, v, s):
        print(v)
        self.visitado[v] = 1
        for i in range(s, self.tamaño + 1):
            if self.adyacencia[v][i] == 1:
                if self.visitado[i] == 0:
                    self.dfs_recursivo(i, i)

    def kruskal(self):
        numero_vertices = CO.eneConjuntos(self.tamaño)
        numero_vertices.inicializa()
        spanning_tree = CO.conjunto()
        i = 0    
        e = 0
        while e < self.tamaño - 1:
            u, v, w = self.lados.retorna_datos(i)
            i = i + 1 
            x = numero_vertices.al_conjunto(u)
            y = numero_vertices.al_conjunto(v)
            if x != y: 
                e = e + 1
                lado = CO.lado(u, v, w)
                spanning_tree.agregar_lado(lado)
                numero_vertices.une_conjunto(x, y)
        return spanning_tree

    def prim(self):
        k = 0
        spanning_tree = CO.conjunto()
        escogido = []
        for i in range(self.tamaño + 1):
            escogido.append(0)
        escogido[1] = 1
        while k < self.tamaño:
            lado = self.escoge_lado(escogido)
            vertice1 = lado.retorna_vertice1()
            vertice2 = lado.retorna_vertice2()
            escogido[vertice1] = 1
            escogido[vertice2] = 1
            k = k + 1
            spanning_tree.agregar_lado(lado)
        return spanning_tree

    def escoge_lado(self, escogido):
        menor = 999999999
        for i in range(self.tamaño + 1):
            if escogido[i] == 1:
                for j in range(self.tamaño + 1):
                    if escogido[j] == 0 and self.costos[i][j] < menor:
                        menor = self.costos[i][j]
                        lado = CO.lado(i, j, menor)
        return lado

    def dikstra_mod(self, n, v, costoMinimo):
        camino = [0]*(self.tamaño + 1)
        ruta = [None]*(self.tamaño + 1)
        for i in range(n + 1):
            costoMinimo[i] = self.costos[v][i]
            ruta[i] = i
        camino[v] = 1
        i = 0
        while(i < n - 1):
            j = 0
            while camino[j] == 1:
                j = j + 1
            w = j
            for i in range(w + 1, n + 1):
                if camino[j] == 0 and costoMinimo[j] < costoMinimo[w]:
                    w = j
            camino[w] = 1
            i = i + 1
            for j in range(n + 1):
                if camino[j] == 0:
                    paso = costoMinimo[w] + self.costos[w][j]
                    if paso < costoMinimo[j]:
                        costoMinimo[j] = paso
                        ruta[j] = w

    #Algoritmo de Warshall
    def cierre_transitivo(self):
        adya_mas = np.zeros((self.tamaño + 1, self.tamaño + 1))
        for i in range(self.tamaño + 1):
            for j in range(self.tamaño + 1):
                adya_mas[i][j] = self.adyacencia[i][j]
        for k in range(self.tamaño + 1):
            for i in range(self.tamaño + 1):
                for j in range(self.tamaño + 1):
                    if adya_mas[i][k] == 1 and adya_mas[k][j] == 1 and i != j:
                        adya_mas[i][j] = 1

    #Algoritmo de Floyd
    def todos_los_caminos_mas_cortos(self):
        menores_costos = np.zeros((self.tamaño + 1, self.tamaño + 1))
        for i in range(self.tamaño + 1):
            for j in range(self.tamaño + 1):
                menores_costos[i][j] = self.costos[i][j]
        for k in range(self.tamaño + 1):
            for i in range(self.tamaño + 1):
                for j in range(self.tamaño + 1):
                    aux = menores_costos[i][k] + menores_costos[k][j]
                    if aux < menores_costos[i][j]:
                        menores_costos[i][j] = aux
