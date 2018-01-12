import sys
import resource
import time
# Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK, (hardlimit, hardlimit))

file = open('SCC.txt', 'r')
# Building graph and graph_rev
graph, graph_rev = {}, {}
for edge in file.read().split("\n"):
    if edge != "":
        tail, head = edge.split(" ")[0], edge.split(" ")[1]
        if tail not in graph:
            graph[tail] = set()
        if head not in graph:
            graph[head] = set()
        graph[tail].add(head)

        if tail not in graph_rev:
            graph_rev[tail] = set()
        if head not in graph_rev:
            graph_rev[head] = set()
        graph_rev[head].add(tail)

print(len(graph_rev.keys()))
print(len(graph.keys()))


# For custom sorting of graph keys
def ft_sort(x):
    global ft
    return ft[x]


global t, s, visited, leaders, ft
t = 0
s = None
visited = set()
leaders = [""] * (len(graph.keys()) + 1)
ft = {}  # Finish times


def dfs_loop(g, key):
    global t, ft, visited, s

    for node in sorted(list(g.keys()), key=key, reverse=True):
        if node not in visited:
            s = node
            dfs(g, node)


def dfs(g, start):
    global t, s, visited, leaders, ft

    visited.add(start)
    leaders[int(start)] = s
    for nxt in g[start] - visited:
        dfs(g, nxt)
    t += 1
    ft[start] = t


def most_common(lst, x):
    # This functions returns the 'x' most common elements from 'lst'
    c = Counter(lst)
    result = []
    for number, count in c.most_common(x):
        result.append(count)
    return result


from collections import Counter


def kosaraju(n):
    global leaders, visited, t
    dfs_loop(graph_rev, int)
    leaders = [""] * (len(graph.keys()) + 1)
    visited = set()
    t = 0
    dfs_loop(graph, ft_sort)
    return most_common(leaders, n)


print(kosaraju(5))
print("done")
