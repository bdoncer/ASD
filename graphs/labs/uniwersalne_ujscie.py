def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        sem = 0
        for j in range(len(G[i])):
            if G[i][j] == 1:
                neigh = j
                sem += 1
                if visited[neigh] == False:
                    parent[neigh] = i
                    res = DFS_visit(G, neigh)
                    if res != None:
                        return res
        if sem == 0:
            return i
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    x = DFS_visit(G,0)

_G = [
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]