from math import inf
from queue import PriorityQueue

def Dijkstra(G,s):
    n = len(G)
    visited = [[False,False,False] for _ in range(n)]
    d = [[inf,inf,inf] for _ in range(n)]
    d[s][0] = 0
    d[s][1] = 0
    d[s][2] = 0
    Q = PriorityQueue()
    Q.put((0, s,1))
    Q.put((0,s,5))
    Q.put((0,s,8))
    while Q.qsize() != 0:
        dist,v,opt = Q.get()
        k = option(opt)
        if visited[v][k] == False:
            visited[v][k] = True
            for i in range(len(G[v])):
                neigh = i
                weight = G[v][i]
                k = option(weight)
                if weight != opt and weight != 0:
                    if visited[neigh][k] == False:
                        if d[neigh][k] > dist + weight:
                            d[neigh][k] = dist + weight
                            Q.put((d[neigh][k],neigh,weight))
    return d

def option(a):
    if a == 1:return 0
    if a == 5:return 1
    if a == 8:return 2
G = [[0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]]
print(Dijkstra(G,5))