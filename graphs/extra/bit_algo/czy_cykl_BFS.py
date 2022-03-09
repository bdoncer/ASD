from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    d = [-1]*n
    parent = [None]*n
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if visited[G[u][i]] == True and G[u][i] != parent[u]:
                return True
            if visited[G[u][i]] == False:
                visited[G[u][i]] = True
                parent[G[u][i]] = u
                Q.put(G[u][i])
    return False


G = [[1],[0,2],[1,3],[2]]
print(BFS(G,0))



