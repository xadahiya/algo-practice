import sys, resource, time

# Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

file = open('SCC.txt', 'r')

## Building graph
graph = {}
for edge in file.read().split("\n"):
    if edge != "":
        tail, head = edge.split(" ")[0], edge.split(" ")[1]
        if tail not in graph:
            graph[tail] = set()
        if head not in graph:
            graph[head] = set()
        graph[tail].add(head)


file = open('SCC.txt', 'r')

graph_rev = {}
for edge in file.read().split("\n"):
    if edge != "":
        tail, head = edge.split(" ")[1], edge.split(" ")[0]
        if tail not in graph_rev:
            graph_rev[tail] = set()
        if head not in graph_rev:
            graph_rev[head] = set()
        graph_rev[tail].add(head)

print(len(graph_rev.keys()))
print(len(graph.keys()))

global t, s, visited, leaders, ft
t = 0
s =  None
visited = set()
leaders = {}
ft = {}
def dfs_loop(g, key):
    global t, ft
    global visited
    global s
    for node in sorted(list(graph_rev.keys()), key = key, reverse = True):
        print(node)
        if node not in visited:
             s = node
             dfs(g, node)


def dfs(g, start):
    global t, s, visited, leaders, ft
    visited.add(start)
    if s not in leaders:
        leaders[s] = [start]
    else:
        leaders[s].append(start)
    for nxt in g[start] - visited:
        dfs(g, nxt)
    t += 1
    ft[start] = t

def ft_sort(x):
    global ft
    return ft[x]

dfs_loop(graph_rev, int)

leaders = {}
visited = set()
t = 0


dfs_loop(graph, ft_sort)

print(','.join(str(len(leaders[k])) for k in sorted(leaders, key=lambda k: len(leaders[k]), reverse=True)))
