
#Autor: Daniel Brand Taborda


class NodoEnhebrado:
    def __init__(self, d):
        self.dato = d
        self.Li = None
        self.Bi = 0
        self.Ld = None
        self.Bd = 0

    def set_dato(self, d):
        self.dato = d

    def set_Li(self, Li):
        self.Li = Li

    def set_Bi(self, Bi):
        self.Bi = Bi

    def set_Ld(self, Ld):
        self.Ld = Ld

    def set_Bd(self, Bd):
        self.Bd = Bd

    def get_dato(self):
        return self.dato

    def get_Li(self):
        return self.Li

    def get_Bi(self):
        return self.Bi

    def get_Ld(self):
        return self.Ld

    def get_Bd(self):
        return self.Bd

class ArbolEnhebradoPreorden:
    def __init__(self):
        self.raiz = NodoEnhebrado(None)
        self.raiz.set_Li(self.raiz)
        self.raiz.set_Bd(1)
        self.raiz.set_Ld(self.raiz)
        self.lista = []
        self.lista.append(self.raiz)
        self.lista_hojas = []

    def es_vacio(self):
        return self.raiz.get_Bi() == 0

    def agregar_dato(self, d):
        n = NodoEnhebrado(d)
        if self.es_vacio():
            self.raiz.set_Bi(1)
            self.raiz.set_Li(n)
            return
        p = self.raiz.get_Li()
        q = None
        while p is not None:
            if p.get_dato() == d: return
            q = p
            if d >= p.get_dato():
                p = p.get_Ld()
            else:
                p = p.get_Li()
        if d > q.get_dato():
            q.set_Ld(n)
            q.set_Bd(1)
        else:
            q.set_Li(n)
            q.set_Bi(1)

    def listar_preorden(self, R):
        if R is None: return
        self.lista.append(R)
        self.listar_preorden(R.get_Li())
        self.listar_preorden(R.get_Ld())

    def enhebrar_preorden(self):
        if self.es_vacio(): return
        self.listar_preorden(self.raiz.get_Li())
        for i in range(len(self.lista)):
            if self.lista[i].get_Bi == 0: self.lista[i].set_Li(self.lista[i-1])
            if self.lista[i].get_Bd == 0:
                if i == len(self.lista) - 1: self.lista[i].set_Ld(self.lista[0])
                else: self.lista[i].set_Ld(self.lista[i+1])

    def listar_hojas(self, R, c):
        if R.get_Bd() == 0 and R.get_Bi() == 0:
            self.lista_hojas.append([R, c])
            return
        if R.get_Bi() == 1: self.listar_hojas(R.get_Li(), c + 1)
        if R.get_Bd() == 1: self.listar_hojas(R.get_Ld(), c + 1)

print("Bienvenido, a continuación ingrese valores ENTEROS para llenar el árbol binario enhebrado.")
arbol = ArbolEnhebradoPreorden()
n = int(input("Ingrese la cantidad de valores que desea ingresar al árbol: "))
p = 0
while p != n:
    valor = int(input("Ingresar dato: "))
    arbol.agregar_dato(valor)
    p = p + 1
arbol.enhebrar_preorden()
arbol.listar_hojas(arbol.raiz.get_Li(), 1)
a = arbol.lista_hojas
print("La distancia entre valores del árbol se mide dependiendo del nivel en el que se encuentre la hoja.")
print("Si el valor es positivo, significa que el nivel del valor es mayor.")
print("Si el valor es 0, significa que los valores están en el mismo nivel.")
print("si el valor es negativo, significa que el nivel del valor es menos.")
for i in range(len(a) - 1):
    for b in range(i+1, len(a) - 1):
        m = str(a[i][1] - a[b][1])
        a1 = str(a[i][0].get_dato())
        a2 = str(a[b][0].get_dato())
        print("La distancia entre el dato " + a1 + " y el dato " + a2 + " es: " + m)

print("Programa realizado por: Daniel Brand Taborda")