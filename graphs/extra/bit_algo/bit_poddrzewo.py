def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        suma = 1
        for neigh in G[i]:
            if visited[neigh] == False:
                suma += DFS_visit(G, neigh)
        d[i] = suma
        return suma

    n = len(G)
    visited = [False]*n
    d = [None]*n

    DFS_visit(G,5)
    print(d)



G = [[1],[0,4],[4],[4],[1,2,3],[4,6],[5,7],[6,8],[7]]
DFS(G)