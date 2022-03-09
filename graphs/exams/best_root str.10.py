def DFS(G,s):
    def DFS_visit(G, i):
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                d[neigh] = d[i]+1
                parent[neigh] = i
                DFS_visit(G, neigh)
    n = len(G)
    visited = [False]*n
    d = [0]*n
    parent = [None]*n
    DFS_visit(G,s)
    return d,parent

def best_root(A):
    dist,parent = DFS(A,0)
    res = [-1,-1]
    for i in range(len(A)):
        if dist[i] > res[1]:
            res = i,dist[i]
    dist,parent = DFS(A,res[0])
    res = [-1, -1]
    for i in range(len(A)):
        if dist[i] > res[1]:
            res = i,dist[i]
    lenght = res[1]/2
    index = res[0]
    while lenght > 0:
        index = parent[index]
        lenght -=1
    return index
L = [[2],[2],[0,1,3],[2,4],[3,5,6],[4],[4]]
print(best_root(L))