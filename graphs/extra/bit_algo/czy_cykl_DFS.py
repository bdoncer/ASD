def DFS_visit(G,i,visited,parent):
    visited[i] = True
    for neigh in range(len(G[i])):
        if visited[G[i][j]] == True and G[i][j] != parent[i]:
            return True
        if visited[G[i][j]] == False:
            parent[G[i][j]] = i
            DFS_visit(G,G[i][j],visited,parent)
    return False

def DFS(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    for i in range(len(G)):
        if visited[i] == False:
            if DFS_visit(G,i,visited,parent) == True:
                return True
    return False


G = [[1,3],[3],[],[0],[],[]]
print(DFS(G))



