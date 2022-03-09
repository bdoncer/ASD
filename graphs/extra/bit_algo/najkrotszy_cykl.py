from math import inf
from queue import PriorityQueue

def Dijkstra(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, s))
    while Q.qsize() != 0:
        dist,v = Q.get()
        if v != s:
            visited[v] = True
        for i in range(len(G[v])):
            neigh = G[v][i][0]
            weight = G[v][i][1]
            if visited[neigh] == False:
                if parent[v] == s and neigh == s:
                    continue

                if d[neigh] > dist + weight:
                    d[neigh] = dist + weight
                    parent[neigh] = v
                    Q.put((d[neigh],neigh))
    return d[s]

def main(G):
    res = inf
    for i in range(len(G)):
        x = Dijkstra(G,i)
        print(x)
        if x < res:
            res = x
    return x
G = [[[1,1],[3,3]],[[0,1],[3,1],[2,2],[4,7]],[[1,2],[4,2]],[[0,3],[1,1],[4,5]],[[2,2],[1,7],[3,5]]]
main(G)