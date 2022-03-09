def jak_daleko(x1,y1,x2,y2,Z):
    res = (x2-x1)**2+(y2-y1)**2
    res = res**(1/2)
    if res <= Z:
        return 1
    if res <= 2*Z:
        return 2
    return -1
def stworz_graf(T,Z):
    n = len(T)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if i != j:
                x = jak_daleko(T[i][0],T[i][1],T[j][0],T[j][1],Z)
                if x != -1:
                    G[i].append([j,x,x])
                    G[j].append([i,x,x])
    return G
from queue import Queue
def zeglarz(T,s,t,Z):
    G = stworz_graf(T,Z)
    Q = Queue()
    visited = [False]*(len(G))
    dist = [-1]*(len(G))
    visited[s] = True
    dist[s] = 0
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for i in range(len(G[v])):
            neigh = G[v][i][0]
            type = G[v][i][1]
            prev_type = G[v][i][2]
            if visited[neigh] == False:
                if type == 1:
                    visited[neigh] = True
                    if neigh == t:
                        dist[t] = dist[v]+1
                    elif prev_type == 1:
                        dist[neigh] = dist[v] + 1
                    elif prev_type == 2:
                        dist[neigh] = dist[v] + 2
                    Q.put(neigh)
                if type == 2:
                    G[v][i][1] -= 1
                    Q.put(v)
    print(dist)

def zeglarz_2(T,s,t,Z):
    G = stworz_graf(T,Z)
    Q = Queue()
    for line in G:
        print(line)
    visited = [[False,False] for _ in range(len(G))]
    dist = [[-1,-1] for _ in range(len(G))]
    visited[s][0] = True
    dist[s][0] = 0
    visited[s][1] = True
    dist[s][1] = 0
    Q.put((s,0))
    while not Q.empty():
        v,type = Q.get()
        for i in range(len(G[v])):
            neigh = G[v][i][0]
            weight = G[v][i][1]
            if neigh == t:
                print(dist)
                return dist[v][type]+1
            if visited[neigh][0] == False and weight == 1:
                visited[neigh][0] = True
                dist[neigh][0] = dist[v][type] + 1
                Q.put((neigh,0))
            if visited[neigh][1] == False and weight == 2:
                    visited[neigh][1] = True
                    dist[neigh][1] = dist[v][type] + 2
                    Q.put((neigh,1))

    print(dist)

#[0, 1, 2, 2, 2, 4, 6, 4, 6, 5, 6, 7, 7, 8, 8, 8]


_islands = [
    [0, 0],
    [0.5, 0.5],
    [1, 1],
    [1, 2],
    [2, 1],
    [2.5, 2.5],
    [2.5, 4],
    [3.5, 2.5]
]
print(zeglarz(_islands,0,7,1.2))