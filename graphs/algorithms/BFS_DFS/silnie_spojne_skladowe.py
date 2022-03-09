def DFS(G):
    time = 0
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = True
        for j in range(len(G[i])):
            if G[i][j] == 1:
                neigh = j
                if visited[neigh] == False:
                    DFS_visit(G, neigh)
        times[i] = time
        time += 1
    n = len(G)
    visited = [False]*n
    times = [-1]*n
    for i in range(len(G)):
        if visited[i] == False:
            DFS_visit(G,i)
    return times

def DFS_reversed(G,times):
    def DFS_visit2(G, i,number):
        visited[i] = number
        for j in range(len(G[i])):
            if G[j][i] == 1:
                neigh = j
                if visited[neigh] == False:
                    DFS_visit2(G, neigh,number)
    n = len(G)
    visited = [False]*n
    number = 1
    while czy_skonczone(visited)==False:
        res = -1
        index = -1
        for i in range(len(times)):
            if visited[i] == False and times[i] > res:
                res = times[i]
                index = i
        DFS_visit2(G,index,number)
        number += 1
    print(visited)

def czy_skonczone(T):
    for i in range(len(T)):
        if T[i] == False:
            return False
    return True
def silna_skladowa(G):
    times = DFS(G)
    DFS_reversed(G,times)

_G1 = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 0]]

silna_skladowa(_G1)