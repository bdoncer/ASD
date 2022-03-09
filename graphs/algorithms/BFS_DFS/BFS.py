#V+E/V2
from queue import Queue
def BFS_lista(G,s):
    Q = Queue()
    visited = [False] * len(G)
    dist = [-1] * len(G)
    parent = [None] * len(G)
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for neigh in G[v]:
            if visited[neigh] == False:
                visited[neigh] = True
                dist[neigh] = dist[v] + 1
                parent[neigh] = v
                Q.put(neigh)

from queue import Queue
def BFS_matrix(G,s):
    Q = Queue()
    visited = [False] * len(G)
    dist = [-1] * len(G)
    parent = [None] * len(G)
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for neigh in range(len(G[v])):
            if G[v][neigh] != 0 and visited[neigh] == False:
                visited[neigh] = True
                dist[neigh] = dist[v] + 1
                parent[neigh] = v
                Q.put(neigh)


