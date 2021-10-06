#Grafo como multilistas de adyacencia
class nodoMultilista:
    def __init__(self, vi, vj):
        self.vi = vi
        self.vj = vj
        self.sw = 0
        self.ligaVi = None
        self.ligaVj = None

    def asigna_vi(self, vi):
        self.vi = vi

    def asigna_vj(self, vj):
        self.vj = vj

    def asigna_LVi(self, ligaVi):
        self.ligaVi = ligaVi

    def asigna_LVj(self, ligaVj):
        self.ligaVj = ligaVj

    def asigna_sw(self, sw):
        self.sw = sw

    def retorna_vi(self):
        return self.vi

    def retorna_vj(self):
        return self.vj

    def retona_LVi(self):
        return self.ligaVi

    def retona_LVj(self):
        return self.ligaVj

    def retorna_sw(self):
        return self.sw

class grafoMLA:
    def __init__(self, tamaño):
        self.vector = [None]*(tamaño + 1)
        self.visitado = [0]*(tamaño + 1)
        self.cola = []

    def conectar_nodos(self, nodo1, nodo2):
        x = nodoMultilista(nodo1, nodo2)
        x.asigna_LVi(self.vector[nodo1])
        x.asigna_LVj(self.vector[nodo2])
        self.vector[nodo1] = x
        self.vector[nodo2] = x

    def dfs(self):
        self.mostrar_dfs(0)

    def mostrar_dfs(self, v):
        print(v)
        self.visitado[v] = 1
        p = self.vector[v]
        while p is not None:
            if p.retorna_vi() == v:
                i = p.retorna_vj()
                if self.visitado[i] == 0:
                    self.mostrar_dfs(i)
                p = p.retorna_LVi
            else:
                i = p.retorna_vi()
                if self.visitado[i] == 0:
                    self.mostrar_dfs(i)
                p = p.retorna_LVj()

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
                if p.retorna_vi() == v:
                    i = p.retorna_vj()
                    p = p.retorna_LVi()
                else:
                    i = p.retorna_vj()
                    p = p.retorna_LVj()
                if self.visitado[i] == 0:
                    self.visitado[i] = 1
                    self.cola.append(i)