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
            if visited[neigh] == True and dist[v] == dist[neigh]:
                return True
    return False
G = [[1,3,2],[2,0],[3,1,0],[2,0]]
print(BFS_lista(G,0))