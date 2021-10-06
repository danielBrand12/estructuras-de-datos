class conjunto:
    def __init__(self):
        self.conjunto = []

    def agregar_lado(self, lado):
        self.conjunto.append(lado)

    def ordernar_por_costo(self):
        self.conjunto.sort(key=self.costo)

    def costo(self, x):
        return x.retorna_costo()

    def retorna_datos(self, i):
        return self.conjunto[i].retorna_vertice1(), self.conjunto[i].retorna_vertice2(), self.conjunto[i].retorna_costo()

class eneConjuntos:
    def __init__(self, tamaño):
        self.eneConjunto = []
        self.rango = []
        self.tamaño = tamaño

    def inicializa(self):
        for vertice in range(self.tamaño + 1):
            self.eneConjunto.append(vertice)
            self.rango.append(0)

    def al_conjunto(self, vertice):
        if self.eneConjunto[vertice] == vertice:
            return vertice
        return self.al_conjunto(self.eneConjunto[vertice])

    def une_conjunto(self, conjunto1, conjunto2):
        x = self.al_conjunto(conjunto1)
        y = self.al_conjunto(conjunto2)

        if self.rango[x] < self.rango[y]:
            self.eneConjunto[x] = y
        elif self.rango[x] > self.rango[y]:
            self.eneConjunto[y] = x
        else:
            self.eneConjunto[y] = x
            self.rango[x] += 1


class lado:
    def __init__(self, nodo1, nodo2, costo):
        self.nodo1 = nodo1
        self.nodo2 = nodo2
        self.costo = costo

    def retorna_costo(self):
        return self.costo

    def retorna_vertice1(self):
        return self.nodo1

    def retorna_vertice2(self):
        return self.nodo2

l1 = lado(1,2,6)
l2 = lado(1,3,7)
l3 = lado(1,4,3)
l4 = lado(2,3,4)
l5 = lado(2,4,1)
l6 = lado(3,4,10)

con1 = conjunto()
con1.agregar_lado(l1)
con1.agregar_lado(l2)
con1.agregar_lado(l3)
con1.agregar_lado(l4)
con1.agregar_lado(l5)
con1.agregar_lado(l6)

con1.ordernar_por_costo()
for i in range(len(con1.conjunto)):
    print(con1.conjunto[i].retorna_vertice1(), con1.conjunto[i].retorna_vertice2())


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        result = []  # This will store the resultant MST

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            print(parent, x,y)

            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                print(rank)
            # Else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Function call
g.KruskalMST()
