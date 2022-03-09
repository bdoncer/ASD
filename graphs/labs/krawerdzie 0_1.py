from collections import deque
def BFS(G,s,e):
    Q = deque()
    n = len(G)
    visited = [False]*n
    visited[s] = 0
    Q.append(s)
    while Q:
        i = Q.popleft()
        for j in range(len(G[i])):
            if G[i][j] != -1:
                neigh = j
                if visited[neigh] == False:
                    visited[neigh] = visited[i] + G[i][neigh]
                    if G[i][neigh] == 0:
                        Q.appendleft(neigh)
                    else:
                        Q.append(neigh)
                else:
                    if visited[i]+G[i][neigh] < visited[neigh]:
                        visited[neigh] = visited[i]+G[i][neigh]
    return visited[e]




G = [[-1,0,-1,-1,1,-1],[-1,-1,1,0,-1,-1],[-1,-1,-1,-1,-1,1],[-1,-1,0,-1,-1,-1],[-1,-1,-1,-1,-1,1],[-1,-1,-1,-1,-1,-1]]
print(BFS(G,0,5))


