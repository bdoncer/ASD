from queue import Queue
def BFS(G,s,t):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    values = [0]*n
    values[s] = 1
    Q.put(s)
    while not Q.empty():
        i = Q.get()
        for neigh in G[i]:
            values[neigh] += values[i]
            Q.put(neigh)
        if i != t:
            values[i] = 0
    print(values)

_G = [
    [1,2,3],
    [3],
    [3, 4,],
    [5],
    [3, 5],
    [],
]
BFS(_G,0,5)