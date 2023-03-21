import heapq

class Graph:
    def __init__(self, vertices: int = 0, arestas: int = 0, ListaDe_Adjacencia: list[list[tuple[int, int]]] = [], ListaDe_Vertices: list[list[str, str, int, int, list[str]]] = []):
        self.vertices = vertices
        self.arestas = arestas
        self.ListaDe_Adjacencia = ListaDe_Adjacencia
        self.ListaDe_Vertices = ListaDe_Vertices
        if (ListaDe_Vertices == []):
            for i in range(self.vertices):
                self.ListaDe_Vertices.append([])
        if (ListaDe_Adjacencia == []):
            for i in range(self.vertices):
                self.ListaDe_Adjacencia.append([])

    def read_file(self, file_name):
        with open(file_name, encoding="utf8") as file:
            i = 0
            for line in file:
                i += 1
                if(i == 1):
                    self.ListaDe_Vertices.append([None, 's', 0, 0, [None]])
                    self.vertices += 1
                else:
                    aux = line.split(',')
                    inteiro2 = int(aux[2])
                    inteiro3 = int(aux[3])
                    string = aux[4].strip()
                    if(string == ''):
                        string = None
                        self.ListaDe_Vertices.append([aux[0], aux[1], inteiro2, inteiro3, [string]])
                        self.vertices += 1
                    else:
                        vetString = string.split(';')
                        self.ListaDe_Vertices.append([aux[0], aux[1], inteiro2, inteiro3, vetString])
                        self.vertices += 1
            self.ListaDe_Vertices.append([None, 't', 0, 0, None])
            self.vertices += 1
        self.ListaDe_Adjacencia = [[] for i in range(self.vertices)]
        for u in range(1, self.vertices -1):
            v = self.vertices -1
            self.add_directed_edge(u, v, self.ListaDe_Vertices[u][3])


    def AuxAresta(self, string):
        for u in range(1, self.vertices):
            if(string == self.ListaDe_Vertices[u][0]):
                return u

    def add_Aresta(self):
        for v in range(1, self.vertices-1):
            if(self.ListaDe_Vertices[v][4] == [None]):
                self.add_directed_edge(0, v, 0)
            else:
                string = self.ListaDe_Vertices[v][4]
                num = len(string)
                teste = self.ListaDe_Vertices[v][3]
                for aux in range(num):
                    u = self.AuxAresta(string[aux])
                    self.add_directed_edge(u, v, self.ListaDe_Vertices[u][3])

    def add_directed_edge(self, u: int, v: int, w: int):
        if(u >= 0 and u < self.vertices and v >= 0 and v < self.vertices):
            self.ListaDe_Adjacencia[u].append((v, w))
            self.arestas += 1
            return
        print(f"Node u={u} or v={v} is out of allowed range (0, {self.vertices - 1})")


    def Ordenar_ListaDe_Adjacencia(self):
        for i in range(len(self.ListaDe_Adjacencia)):
            self.ListaDe_Adjacencia[i].sort()


    def dijkstra_pq(self, s):
        dist = [float("-inf")] * self.vertices
        pred = [-1] * self.vertices
        pq = []
        heapq.heapify(pq)  # Empty priority queue
        dist[s] = 0
        heapq.heappush(pq, [0, s])
        while len(pq) != 0:
            [min_dist, u] = heapq.heappop(pq)
            for (v, w) in self.ListaDe_Adjacencia[u]:
                if dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(pq, [dist[v], v])
        return dist, pred


    def Rec_Caminho(self, s, t, pred):
        C = [t]
        aux = t
        while(aux != s):
            aux = pred[aux]
            C.insert(0, aux)
        return C


    def Caminho_Critico(self):
        aux = self.dijkstra_pq(0)
        distancia = aux[0]
        predecessor = aux[1]
        predecessor = self.Rec_Caminho(0, self.vertices - 1, predecessor)
        maior = distancia[0]
        for i in range(1, len(distancia)):
            if(maior < distancia[i]):
                maior = distancia[i]
        nome = []
        for j in predecessor:
            nome.append(self.ListaDe_Vertices[j][1])

        return maior, predecessor, nome[1:len(nome)-1]