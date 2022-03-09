#V+E/V2
def DFS_lista(G):
    time_odwiedzenia = 0
    time_przetworzenia = 0

    def DFS_visit(G,v):
        nonlocal time_odwiedzenia
        nonlocal time_przetworzenia
        time_odwiedzenia += 1
        time_o[v] = time_odwiedzenia
        visited[v] = True
        for neigh in G[v]:
            if visited[neigh] == False:
                parent[neigh] = v
                DFS_visit(G,neigh)
        time_przetworzenia += 1
        time_p[v] = time_przetworzenia

    visited = [False] * len(G)
    parent = [None] * len(G)
    time_o = [-1] * len(G)
    time_p = [-1] * len(G)
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)


def DFS_matrix(G):
    time_odwiedzenia = 0
    time_przetworzenia = 0
    def DFS_visit(G, v):
        nonlocal time_odwiedzenia
        nonlocal time_przetworzenia
        time_odwiedzenia += 1
        time_o[v] = time_odwiedzenia
        visited[v] = True
        for neigh in range(len(G[v])):
            if G[v][neigh] != 0  and visited[neigh] == False:
                parent[neigh] = v
                DFS_visit(G, neigh)
        time_przetworzenia += 1
        time_p[v] = time_przetworzenia
    visited = [False] * len(G)
    parent = [None] * len(G)
    time_o = [-1] * len(G)
    time_p = [-1] * len(G)
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G, i)

