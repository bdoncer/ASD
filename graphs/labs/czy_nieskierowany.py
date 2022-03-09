from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G)
    Q.put(s)
    stopnie = [0]*n
    V = [[0]*n for _ in range(n)]
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            stopnie[u] += 1
            if V[u][neigh] == 0:
                V[neigh][u] = 1
                Q.put(neigh)
    for i in range(n):
        if stopnie[i] != len(G[i]):
            return False
    return True


G = [[1,4],[4,0,2],[1,3],[4],[1,0,3]]
print(BFS(G,0))



