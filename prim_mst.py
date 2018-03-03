file = open('prim_edges.txt')

content = file.readlines()

contents = [tuple(int(a) for a in x.strip().split(" ")) for x in content[1:]]

##Building the graph in adjacent list form

graph = {}
for i in contents:
    if i[0] in graph:
        graph[i[0]].append((i[1], i[2]))
    else:
        graph[i[0]] = [(i[1], i[2])]

    if i[1] in graph:
        graph[i[1]].append((i[0], i[2]))
    else:
        graph[i[1]] = [(i[0], i[2])]


## Simple prims algo (without using heap)

X = [list(graph.keys())[0]]
T = []

while len(X) < 500:

    lst = []
    for n in X:
        lst += graph[n]

    fil_lst = sorted(filter(lambda x : x[0] not in X, lst), key= lambda x : x[1])
    X.append(fil_lst[0][0])
    T.append(fil_lst[0][1])

print(sum(T))


##TODO With heap

