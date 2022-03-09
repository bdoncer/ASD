from math import inf
from queue import PriorityQueue
#Alicja zaczyna
#Alicja ma przejechac jak najmniej km
def alicja_bob(G,s,t):
    n = len(G)
    #do wierzcholka przyjechala alicja,do wierzcholka przyjechal bob
    visited = [[False]*2 for _ in range(n)]
    d = [[inf]*2 for _ in range(n)]
    d[s][1] = 0
    Q = PriorityQueue()
    Q.put((0, s,1))
    while Q.qsize() != 0:
        dist,v,kto = Q.get()
        if visited[v][kto] == False:
            visited[v][kto] = True
            for i in range(len(G[v])):
                neigh = G[v][i][0]
                weight = G[v][i][1]
                if kto == 0: # do wierzcholka przyjechala Alicja
                    if visited[neigh][1] == False:
                        if d[neigh][1] > dist:
                            d[neigh][1] = dist
                            Q.put((d[neigh][1],neigh,1))
                if kto == 1: #do wierzcholka przyjechal bob
                    if visited[neigh][0] == False:
                        if d[neigh][0] > dist+weight:
                            d[neigh][0] = dist+weight
                            Q.put((d[neigh][0],neigh,0))
    return d[t]

G = [[[1,40],[4,20]],[[3,100]],[],[[2,20]],[[2,20],[3,20]]]
print(alicja_bob(G,0,2))

