import random
import math

class Vertex:
    """Vertex Class for Undirected graph."""
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def addNeighbor(self, nbr, n):
        if nbr.getId() != self.id:
            self.connected_to[nbr] = n

    def improveNeighborConnection(self, nbr, n):
        if nbr in self.connected_to:
            self.connected_to[nbr] += n
        else:
            self.addNeighbor(nbr, n)

    def removeNeighbor(self, nbr):
        self.connected_to.pop(nbr)

    def __str__(self):
        return str(self.id) + " connected to " + str([x.id for x in self.connected_to])

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

    def removeVertex(self, key):
        if key in self.vertList.keys():
            self.numVertices -= 1
            self.vertList.pop(key, None)


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

        self.vertList[a].addNeighbor(self.vertList[b], 1)
        self.vertList[b].addNeighbor(self.vertList[a], 1)

    def getVertices(self):
        return self.vertList.keys()

    def getNumVertices(self):
        return self.numVertices

    def getEdges(self):
        edges = []
        for v in self.vertList.values():
            for w in v.getConnections():
                if v.getId() != w.getId():
                    # edges.append((min(v.getId(), w.getId()), max(v.getId(), w.getId())))
                    edges.append((v.getId(), w.getId()))
        return edges

    def contract(self, edge):
        """Merge the elements with edge into one."""
        # (1,37)
        # Say we keep the node with min key value and merge everything into it.
        a, b = edge
        # print(self.vertList)
        ## Add all of other_node connections to final_node
        for w in list(self.vertList[b].getConnections()):
            self.vertList[a].improveNeighborConnection(w, self.vertList[b].getConnections()[w])
            # replace the other_node by final_node in all connections
            w.improveNeighborConnection(self.vertList[a], w.getConnections()[self.vertList[b]])
            w.removeNeighbor(self.vertList[b])



        self.removeVertex(b)



    def __iter__(self):
        return iter(self.vertList.values())

# print(alist)

def buildGraph(filename):
    textfile = open(filename, 'r')
    alist = [a.split("\t") for a in textfile.read().split("\n") if a != ""]

    g = Graph()
    for i in range(1, 201):
        g.addVertex(i)

    for item in alist:
        for a in item:
            g.addEdge(item[0], a)

    return g
# for v in g:
#     for w in v.getConnections():
#          print("( %s , %s )" % (v.getId(), w.getId()))

# print(g.getVertex("1"))
# print(g.contract(("1","37")))
# print([g.getVertex("1")[x] for x in g.getVertex("1").getConnections()])
# print(g.getNumVertices())
#
# for i in range(1,5):
#     g.addVertex(i)
#
# g.addEdge(1,2)
# g.addEdge(2,4)
# g.addEdge(4,3)
# g.addEdge(3,1)
# g.addEdge(2,3)
# print("333", g.getVertex(3).getConnections())
# print(g.contract((1,3)))
#
# print("333", g.getVertex(1).getConnections())
#
#
# for v in g:
#     for w in v.getConnections():
#          print("( %s , %s )" % (v.getId(), w.getId()))
#

def kargerMinCut(g):
    while g.getNumVertices() > 2:
        edge = random.choice(g.getEdges())
        g.contract(edge)

    # print(g.getNumVertices(), g.getEdges())
    # return list(g.getVertices())[0]
    for v in g:
        for w in v.getConnections():
             return v.getConnections()[w]
g = buildGraph('kargerMinCut.txt')
def kargerMinCutIterator(g):
    minCutVal = None
    n = int((200**2)*math.log(200))
    while n > 0:


        temp = kargerMinCut(g)
        if minCutVal == None:
            minCutVal = temp
        else:
            if minCutVal > temp:
                minCutVal = temp
        n -= 1
        print(minCutVal, temp)
    return minCutVal


print(kargerMinCutIterator(g))
