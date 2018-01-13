file = open('dijkstraData.txt', 'r')

graph = {}
for i in range(1, 201):
    graph[str(i)] = set()
for line in file.read().split("\n"):
    line = line.split("\t")
    for n in range(1, len(line)):
        if line[n] != "":
            graph[line[0]].add((line[n].split(",")[0], line[n].split(",")[1]))


def dijkstra(graph, s):
    
    X = set(s) ## Vertices done
    A = {} ## For shortest paths
    A[s] = 0
    
    while True:
        min_dis, min_v =  1000000, None

        for x in X:
            for v, l in graph[x]:
                if v not in X and A[x] + int(l) <= min_dis:
                    min_dis = A[x] + int(l)
                    min_v = v
        if min_v != None:
            X.add(min_v)
            A[min_v] = min_dis
        else:
            break
    no_path_vertices = set(graph.keys()) - X
    print(no_path_vertices)
    for vertex in no_path_vertices:
        A[vertex] = 1000000
    return A, X

a, x = dijkstra(graph, '1')
s = "7,37,59,82,99,115,133,165,188,197"
output_keys = s.split(",")
print(",".join([str(a[s]) for s in output_keys]))
print("done")
