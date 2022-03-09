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
    return d,parent
def main(G):
    dist,parent = Dijkstra(G,0)
    ind = -1
    res = 0
    for i in range(len(dist)):
        if dist[i] > res:
            res=dist[i]
            ind = i
    dist, parent = Dijkstra(G, ind)
    sciezka = []
    a = -1
    res = 0
    for i in range(len(dist)):
        if dist[i] > res:
            res = dist[i]
            ind = i

    while ind != a:
        sciezka.append(ind)
        ind = parent[ind]
    print(sciezka)
    best= res//2
    for i in range(1,len(sciezka)):
        prev_best = best
        best -= krawedz(sciezka[i-1],sciezka[i],G)
        if best < 0:
            if abs(prev_best) < abs(best):
                print(sciezka[i-1])
            else:
                print(sciezka[i])
            break


def krawedz(od,do,G):
    for v in G[od]:
        if v[0] == do:
            return v[1]



graf = [[[1, 2]], [[0, 2], [2, 3], [5, 8]], [[1, 3], [3, 7], [4, 5]], [[2, 7]],
            [[2, 5]], [[1, 8], [6, 3], [7, 6]], [[5, 3]], [[5, 6], [8, 7], [9, 13], [11, 5]],
            [[7, 7]], [[7, 13], [10, 4]], [[9, 4]], [[7, 5], [12, 2]], [[11, 2]]]
main(graf)
