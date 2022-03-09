from math import inf
from queue import PriorityQueue

def Dijkstra(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while Q.qsize() != 0:
        krawedz,v = Q.get()
        if visited[v] == False:
            visited[v] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if visited[neigh] == False:
                    if d[neigh] > max(krawedz,weight):
                        d[neigh] = max(krawedz,weight)
                        Q.put((d[neigh],neigh))
    print(d[4])

G = [[[1,60],[3,120]],[[2,80],[3,70]],[[4,70]],[[4,30]],[]]
Dijkstra(G,0)