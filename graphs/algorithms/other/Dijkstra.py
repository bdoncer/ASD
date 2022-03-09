#ElogV/V2
from math import inf
from queue import PriorityQueue

def Dijkstra(G,s):
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
                    if d[neigh] > dist + weight:
                        d[neigh] = dist + weight
                        parent[neigh] = v
                        Q.put((d[neigh],neigh))

def dijkstra_matrix(G, s):
    n = len(G)
    dist = [[inf] for _ in range(n)]
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist[s][0] = 0
    for i in range(n):
        v = -1
        min_dist = inf
        for j in range(n):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                v = j
        visited[v] = True
        for neigh in range(n):
            if G[v][neigh] > 0 and not visited[neigh] and dist[neigh] > dist[v] + G[v][neigh]:
                dist[neigh] = dist[v] + G[v][neigh]
                parent[neigh] = v
    print(dist)


g1 = [[0, 7, 1, 2, 8],
      [7, 0, 0, 0, 0],
      [1, 0, 0, 1, 0],
      [2, 0, 1, 0, 3],
      [8, 0, 0, 3, 0]]
dijkstra_matrix(g1,0)