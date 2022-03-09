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
    return dist

def srednica(G):
    dist = BFS_lista(G,0)
    index = 0
    max_dist = dist[0]
    for i in range(1,len(dist)):
        if dist[i] > max_dist:
            max_dist = dist[i]
            index = i
    dist = BFS_lista(G,i)
    max_dist = dist[0]
    for i in range(1, len(dist)):
        if dist[i] > max_dist:
            max_dist = dist[i]
    return max_dist

L = [[2],[2],[0,1,3],[2,4],[3]]
print(srednica(L))
