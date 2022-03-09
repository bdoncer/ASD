from queue import Queue
def BFS_lista(G,s):
    Q = Queue()
    visited = [False] * len(G)
    dist = [-1] * len(G)
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for j in range(len(G[v])):
            neigh = G[v][j][0]
            if visited[neigh] == False:
                if G[v][j][2] == 1:
                    visited[neigh] = True
                    dist[neigh] = dist[v] + G[v][j][1]
                    Q.put(neigh)
                else:
                    G[v][j][2] -= 1
                    Q.put(v)
    print(dist)

T = [[[1,1,1]],[[3,1,1],[2,3,3]],[[1,3,3],[3,1,1]],[[1,1,1],[2,1,1],[4,3,3]],[[3,3,3]]]
BFS_lista(T,0)