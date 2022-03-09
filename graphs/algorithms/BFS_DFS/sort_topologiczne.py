def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                DFS_visit(G, neigh)
        lista.append(i)
    n = len(G)
    visited = [False]*n
    lista = []
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    lista.reverse()
    print(lista)


G = [[1,2],[2],[]]
DFS(G)