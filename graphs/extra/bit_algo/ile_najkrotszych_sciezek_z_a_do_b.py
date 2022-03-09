from queue import Queue
from math import inf
def BFS(G,s,e):
    Q = Queue()
    n = len(G) #ilosc wierzcholkow
    visited = [False]*n
    d = [inf]*n
    visited[s] = True
    paths=[0]*n
    d[s] = 0
    paths[s]=1
    Q.put(s)
    while not Q.empty():
        i = Q.get()
        for neigh in G[i]:
            if visited[neigh] == False:
                visited[neigh] = True
                Q.put(neigh)
            if d[neigh] > d[i] + 1:
                d[neigh] = d[i] + 1
                paths[neigh] = paths[i]
            elif d[neigh] == d[i]+1:
                paths[neigh] += paths[i]

    return paths[e]
_G=[
    [1,2],
    [0,3,4],
    [0,3,4],
    [1,4,5],
    [2,3,5],
    [3,4]
]

_G1 = [
    [1,2],
    [0,3],
    [0,3,4],
    [1,5,4,2],
    [2,3,6],
    [3,7],
    [4,7],
    [5,6]
]

print(BFS(_G1,0,5))