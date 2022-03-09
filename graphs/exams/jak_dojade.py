from math import inf
def czy_stacja(P,i):
    for j in range(len(P)):
        if P[j] == i:
            return True
    return False
def Dijkstra(G, P,d,s,t):
    n = len(G)
    dist = [[inf]*(d+1) for _ in range(n)]
    visited = [[False]*(d+1) for _ in range(n)]
    parent = [[-1]*(d+1) for _ in range(n)]

    dist[s][d] = 0
    for i in range((d+1)*n):
        for k in range(d+1):
            u = -1
            najkrotszy = inf
            for j in range(n):
                if visited[j][k] == False and dist[j][k] < najkrotszy:
                    najkrotszy = dist[j][k]
                    u = j
                    typ = k
        visited[u][typ] = True
        for j in range(n):
            if G[u][j] != -1 and j != u and G[u][j] <= d:
                if visited [j][d] == False and czy_stacja(P,j) == True and dist[j][d] > dist[u][typ] + G[u][j]:
                    dist[j][d] = dist[u][typ] + G[u][j]
                    parent[j][d] = u
                weight = G[u][j]
                if czy_stacja(P,j) == False and typ - weight >= 0 and visited[j][typ-G[u][j]] == False and dist[j][typ-G[u][j]] > dist[u][typ] + G[u][j]:
                    dist[j][typ-weight] = dist[u][typ] + G[u][j]
                    parent[j][typ-weight] = u
    res = [inf, inf]
    for i in range(d + 1):
        if dist[t][i] < res[1]:
            res = [i, dist[t][i]]
    if res[1] == inf:
        return None
    typ = res[0]
    index = t
    print(t)
    while (index != s):
        if parent[index][typ] == -1:
            return None
        print(parent[index][typ])
        old_index = index
        index = parent[index][typ]
        if czy_stacja(P,index):
            typ = d
        else:
            typ -= G[index][old_index]

    return dist

G = [[-1,6,-1,5,2],
     [-1,-1,1,2,-1],
     [-1,-1,-1,-1,-1],
     [-1,-1,4,-1,-1],
     [-1,-1,8,-1,-1]]
P = [0,1,3]
print(Dijkstra(G,P,3,0,2))