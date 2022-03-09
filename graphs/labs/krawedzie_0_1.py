from queue import PriorityQueue
def BFS_lista(G,s):
    Q = PriorityQueue()
    visited = [False] * len(G)
    dist = [-1] * len(G)
    parent = [None] * len(G)
    visited[s] = True
    dist[s] = 0
    for next in G[s]:
        Q.put((next[1], s, next[0]))
    while not Q.empty():
        weight,v,neigh = Q.get()
        if visited[neigh] == False:
            visited[neigh] = True
            dist[neigh] = dist[v] + weight
            parent[neigh] = v
            for next in G[neigh]:
                Q.put((next[1],neigh,next[0]))
G = [[[1,0],[2,1]],[[3,1],[2,0]]]