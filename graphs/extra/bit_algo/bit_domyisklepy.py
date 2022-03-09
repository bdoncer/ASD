from queue import Queue
def odleglosci(G,S):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    d = [-1]*n
    for s in S:
        visited[s] = True
        d[s] = 0
        Q.put(s)
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            if visited[neigh] == False:
                visited[neigh] = True
                d[neigh] = d[u] + 1
                Q.put(neigh)
    return d
_G = [
    [1, 5],
    [5, 4, 2],
    [3, 1],
    [2, 4, 10],
    [8, 5, 1, 3],
    [0, 1, 4, 8, 7],
    [7, 11],
    [5, 8, 12, 6],
    [4, 5, 7, 12, 9],
    [8, 10, 13],
    [3, 9, 14],
    [6],
    [7, 8, 13],
    [12, 9, 14],
    [10, 13, 15],
    [14, 16],
    [15, 17],
    [16]
]
S = [3,7,16]
print(odleglosci(_G,S))


