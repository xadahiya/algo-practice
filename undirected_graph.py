class Vertex:
    """Vertex Class for Undirected graph."""
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def addNeighbor(self,nbr):
        self.connected_to[nbr] = 1

    def __str__(self):
        return str(self.id) + "connected to " + [x.id for x in self.connected_to]

    def getConnections(self):
        return self.connected_to

    def getId(self):
        return self.id


class Graph:
    """A undirected graph class."""
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, k):
        return k in self.vertList

    def addEdge(self, a, b):
        if a not in self.vertList:
            self.vertList[a] = Vertex(a)
        if b not in self.vertList:
            self.vertList[b] = Vertex(b)

        self.vertList[a].addNeighbor(self.vertList[b])
        # self.vertList[b].addNeighbor(self.vertList[a])

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(1, 5):
    g.addVertex(i)

print(g.vertList)
g.addEdge(0,1)
g.addEdge(0,5)
#
for v in g:
    for w in v.getConnections():
         print("( %s , %s )" % (v.getId(), w.getId()))
