class ArbolBinarioVector:
    def __init__(self):
        self.arbol = []

    def inorden(self, i):
        if(i <= len(self.arbol)):
            self.inorden(2*i + 1)
            print(self.arbol[i])
            self.inorden(2*i + 2)

    def preorden(self, i):
        if (i <= len(self.arbol)):
            print(self.arbol[i])
            self.inorden(2 * i + 1)
            self.inorden(2 * i + 2)

    def posorden(self,i):
        if (i <= len(self.arbol)):
            self.inorden(2 * i + 1)
            self.inorden(2 * i + 2)
            print(self.arbol[i])

    def hojas(self):
        n = 0
        for i in range(len(self.arbol)):
            if i % 2 == 1:
                if self.arbol[2*i + 1] == None:
                    n = n + 1
            elif i % 2 == 0:
                if self.arbol[2*i + 2] == None:
                    n = n + 1
        return n

    def es_completo(self):
        for i in range(len(self.arbol)):
            if self.arbol[i] == None: return False
        return True

    def grado(self):
       if(self.es_completo() and len(self.arbol) > 3):
           return 2




