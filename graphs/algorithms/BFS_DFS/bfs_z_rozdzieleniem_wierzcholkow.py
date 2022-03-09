from queue import Queue
def BFS_lista(G,s):
    Q = Queue()
    visited = [False] * len(G)
    dist = [-1] * len(G)
    for i in range(len(G)):
        for j in range(len(G[i])):
            G[i][j].append(G[i][j][1])
    for line in G:
        print(line)
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for j in range(len(G[v])):
            neigh = G[v][j][0]
            weight = G[v][j][1]
            stan = G[v][j][2]
            if visited[neigh] == False:
                if stan == 1:
                    visited[neigh] = True
                    dist[neigh] = dist[v] + weight
                    Q.put(neigh)
                if stan != 1:
                    G[v][j][2] -= 1
                    Q.put(v)
    print(dist)


G = [[[3,3]],
     [[3,11],[2,2],[4,7]],
     [[1,2],[4,2]],
     [[0,3],[1,11],[4,5]],
     [[2,2],[1,7],[3,5]]]
BFS_lista(G,0)