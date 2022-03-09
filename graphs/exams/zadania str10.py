def DFS(G):
    def DFS_visit(G, i):
        visited[i] = True
        for j in range(len(G[i])):
            if G[i][j] == 0 or G[i][j] == 2:
                neigh = j
                if visited[neigh] == False:
                    DFS_visit(G, neigh)
        lista.append(i)
    n = len(G)
    visited = [False]*n
    lista = []
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    return lista

def tasks(T):
    return DFS(T)







T = [[0,2,1,1],
     [1,0,1,1],
     [2,2,0,1],
     [2,2,2,0]]
print(tasks(T))