def DFS(G):
    time = 1
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                parent[neigh] = i
                times[neigh] = (time,neigh)
                time += 1
                DFS_visit(G, neigh)

    n = len(G)
    visited = [False]*n
    parent = [None]*n
    times = [-1]*n
    times[0]=(0,0)
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    times.sort()
    for i in range(n-1,-1,-1):
        print(times[i][1])


_G = [
    [1, 4],
    [0, 2],
    [1, 4, 3],
    [2, 6, 5],
    [0, 2, 7],
    [6, 3],
    [5, 3],
    [4]
]
print(DFS(_G))



