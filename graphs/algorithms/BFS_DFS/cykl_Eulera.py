def DFS(G):
    cykl = []
    def DFS_visit(G, i):
        nonlocal cykl
        for j in range(len(G[i])):
            if G[i][j] == 1:
                neigh = j
                G[i][j] = 0
                G[j][i] = 0
                #parent[neigh] = i
                visited[neigh] = True
                DFS_visit(G, neigh)
        cykl.append(i)
    n = len(G)
    visited = [False]*n
    #parent = [None]*n
    DFS_visit(G,0)
    print(cykl)


_G = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]
DFS(_G)