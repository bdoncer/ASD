#ElogV
from math import inf
from queue import PriorityQueue

def Prim(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while Q.qsize() != 0:
        dist,v = Q.get()
        if visited[v] == False:
            visited[v] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if visited[neigh] == False:
                    if d[neigh] > weight:
                        d[neigh] = weight
                        parent[neigh] = v
                        Q.put((d[neigh],neigh))
    print(parent)


_G = [
    [[1, 1], [2, 12]],
    [[0, 1], [2, 7], [3, 5]],
    [[0, 12], [1, 7], [3, 6], [4, 8]],
    [[1, 5], [2, 6], [4, 4], [5, 3000]],
    [[2, 8], [3, 4], [5, 9]],
    [[4, 9], [3, 3000]],
]
print(Prim(_G,0))