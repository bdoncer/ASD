from queue import Queue
from math import inf
def krawedzie_na_liste(T):
    n = len(T)
    maxx = 0
    for i in range(n):
        maxx = max(maxx,T[i][1])
    G = [[] for _ in range(maxx+1)]
    for i in range(n):
        G[T[i][0]].append(T[i][1])
        G[T[i][1]].append(T[i][0])
    return G

def sciezka(T):
    G = krawedzie_na_liste(T)
    print(G)
    Q = Queue()
    n = len(G)
    visited = [False] * n
    d = [-1] * n
    visited[0] = True
    d[0] = 0
    Q.put(0)
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if visited[G[u][i]] == False:
                visited[G[u][i]] = True
                d[G[u][i]] = d[u] + 1
                Q.put(G[u][i])
    d_max = 0
    res = -1
    for i in range(n):
        if d[i] > d_max:
            res = i
            d_max = d[i]
    for i in range(n):
        visited[i] = False
        d[i] = -1
    visited[res] = True
    d[res] = 0
    Q.put(res)
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if visited[G[u][i]] == False:
                visited[G[u][i]] = True
                d[G[u][i]] = d[u] + 1
                Q.put(G[u][i])
    d_max = 0
    for i in range(n):
        if d[i] > d_max:
            d_max = d[i]
    return d_max

tree = [
    [0, 1],
    [0, 2],
    [0, 3],
    [3, 4],
    [3, 5],
    [5, 7],
    [7, 9],
    [7, 10],
    [4, 6],
    [6, 8]
]
print(sciezka(tree))