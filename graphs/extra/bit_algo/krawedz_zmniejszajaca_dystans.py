from queue import PriorityQueue
from math import inf
def Dijkstra(G,s):
    n = len(G)
    #nie uzylam,uzylam
    visited = [[False,False] for _ in range(n)]
    d = [[inf,inf] for _ in range(n)]
    d[s][0] = 0
    Q = PriorityQueue()
    Q.put((0, s,0))
    while Q.qsize() != 0:
        dist,v,option = Q.get()
        if option == 0:
            visited[v][0] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if weight < 0 and visited[neigh][1] == False:
                    if d[neigh][1] > dist - weight:
                        d[neigh][1] = dist - weight
                        Q.put((d[neigh][1], neigh,1))
                else:
                    if visited[neigh][0] == False and d[neigh][0] > dist + weight:
                        d[neigh][0] = dist + weight
                        Q.put((d[neigh][0], neigh,0))
        if option == 1:
            visited[v][1] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if visited[neigh][1] == False:
                    if weight > 0:
                        if d[neigh][1] > dist + weight:
                            d[neigh][1] = dist + weight
                            Q.put((d[neigh][1], neigh, 1))
    print(d)



G = [[[1,1],[3,3]],[[0,1],[3,-1],[2,-2],[4,7]],[[1,-2],[4,2]],[[0,3],[1,-1],[4,-5]],[[2,2],[1,7],[3,-5]]]
Dijkstra(G,0)