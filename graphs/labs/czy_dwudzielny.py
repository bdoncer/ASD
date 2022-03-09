from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    colour = [-1]*n
    parent = [None]*n
    visited[s] = True
    colour[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            if visited[neigh] == False:
                visited[neigh] = True
                if colour[u] == 0:
                    colour[neigh] = 1
                else:
                    colour[neigh] = 0
                for neigh2 in G[neigh]:
                    if visited[neigh2] == True and colour[neigh] == colour[neigh2]:
                        return False
                parent[neigh] = u
                Q.put(neigh)
    return True



G = [[1,3,4],[4,5],[3,5],[0,2],[0,1],[1,2]]
print(BFS(G,0))



