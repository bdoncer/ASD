def DFS(G):
    time = 1
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                times[neigh] = time
                time += 1
                DFS_visit(G, neigh)
    n = len(G)
    visited = [False]*n
    times = [0]*n
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    return times

G = [[1,2,3,4,5],[0,3],[0],[0,1],[0],[0]]
print(DFS(G))