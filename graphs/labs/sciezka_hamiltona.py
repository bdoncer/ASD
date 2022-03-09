def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in range(len(G[i])):
            if G[i][neigh] != 0 and visited[neigh] == False:
                DFS_visit(G, neigh)
            lista.append(i)
    n = len(G)
    visited = [False]*n
    lista = []
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    print(lista)
    lista = reversed(lista)
