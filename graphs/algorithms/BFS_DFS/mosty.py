from math import inf
def DFS_lista(G):
    time = 0
    def DFS_visit(G,v):
        nonlocal time
        time+= 1
        time_o[v] = time
        low[v] = time
        visited[v] = True
        for neigh in G[v]:
            if visited[neigh] == False:
                parent[neigh] = v
                DFS_visit(G,neigh)
                low[v] = min(low[v], low[neigh])
            if visited[neigh] == True and neigh != parent[v]:
                low[v] = min(low[v],time_o[neigh])
    visited = [False] * len(G)
    parent = [None] * len(G)
    time_o = [inf] * len(G)
    low = [inf] * len(G)
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    for i in range(len(G)):
        if time_o[i] == low[i] and parent[i] != None:
            print(i, parent[i])

    print(low,time_o)

G = [[1,2],[0,2],[0,1,3],[2,4,5],[3,5],[3,4,6],[5,7,8],[6,8],[6,7,9],[8]]
#graf = [[1, 6], [0, 2], [1, 3, 6], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]]
DFS_lista(G)