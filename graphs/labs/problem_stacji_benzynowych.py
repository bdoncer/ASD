from math import inf
from queue import PriorityQueue


def Dijkstra(G, P, s, pojemnosc):
    n = len(G)
    visited = [[False] * (pojemnosc + 1) for _ in range(n)]
    d = [[inf] * (pojemnosc + 1) for _ in range(n)]
    d[s][pojemnosc] = 0
    Q = PriorityQueue()
    Q.put((0, s, pojemnosc))
    while Q.qsize() != 0:
        cost, v, bak = Q.get()
        if visited[v][bak] == False:
            visited[v][bak] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if bak - weight >= 0:
                    for ile in range(bak - weight, pojemnosc + 1):
                        if visited[neigh][ile] == False:
                            if d[neigh][ile] > cost + (ile - (bak - weight)) * P[neigh]:
                                d[neigh][ile] = cost + (ile - (bak - weight)) * P[neigh]
                                Q.put((d[neigh][ile], neigh, ile))
    for line in d:
        print(line)

def Dijkstra_2(G,P,s,pojemnosc):
    n = len(G)
    visited = [[False]*(pojemnosc+1) for _ in range(n)]
    d = [[inf]*(pojemnosc+1) for _ in range(n)]
    d[s][pojemnosc] = 0
    Q = PriorityQueue()
    Q.put((0, s,pojemnosc))
    while Q.qsize() != 0:
        dist,v,bak = Q.get()
        if visited[v][bak] == False:
            visited[v][bak] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if bak - weight >= 0 and visited[neigh][bak-weight] == False:
                    if d[neigh][bak-weight] > dist:
                        d[neigh][bak-weight] = dist
                        Q.put((d[neigh][bak-weight],neigh,bak-weight))
                for i in range(bak-weight,pojemnosc+1):
                    if bak - weight >= 0:
                        if visited[neigh][i] == False and d[neigh][i] > d[neigh][bak-weight] + (i-(bak-weight))*P[neigh]:
                            d[neigh][i] = d[neigh][bak - weight] + (i - (bak - weight)) * P[neigh]
                            Q.put((d[neigh][i],neigh,i))
    for line in d:
        print(line)

G = [[[1, 5], [2, 7]], [[0, 5], [2, 3], [3, 5]], [[0, 7], [1, 3], [3, 4]], [[1, 5], [2, 4], [4, 6]], [[3, 6]]]
G1 = [[[1, 7], [2, 7]], [[0, 7], [2, 13], [3, 2]], [[0, 7], [1, 13], [3, 2]], [[1, 2], [2, 2], [4, 5]], [[3, 5]]]
P = [8, 5, 3, 2, 1]
P1 = [8, 1, 3, 10, 1]
Dijkstra(G, P, 0, 7)
Dijkstra_2(G,P,0,7)
