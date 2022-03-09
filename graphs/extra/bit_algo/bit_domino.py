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
        res = 0
        index = -1
        for i in range(len(times)):
            if visited[i] == False and times[i] > res:
                res = times[i]
                index = i
        DFS_visit2(G,index,number)
        number += 1
    return visited, number-1
from queue import Queue
def BFS(G,skladowe,res):
    number = 0
    Q = Queue()
    n = len(G)
    visited = [False]*n
    visited[0] = True
    index = 0
    tam_bylam = [False]*(res+1)
    while czy_skonczone(visited) == False:
        Q.put(index)
        while not Q.empty():
            i = Q.get()
            for j in range(n):
                if G[i][j] == 1:
                    neigh = j
                    tam_bylam[skladowe[neigh]] = True
                    if visited[neigh] == False:
                        if skladowe[i] != skladowe[neigh] and tam_bylam[i]== False:
                            number += 1
                        visited[neigh] = True
                        Q.put(neigh)
        k = 1
        while tam_bylam[k] != False:
            k += 1
        index = k
    return number

def czy_skonczone(T):
    for i in range(len(T)):
        if T[i] == False:
            return False
    return True

def domino(G):
    times = DFS(G)
    skladowe,number = DFS_reversed(G,times)
    zaoszczedzone = BFS(G,skladowe,number)
    print(number,zaoszczedzone)
    return number - zaoszczedzone


G = [[0,1,0,0,0,0],
[0,0,1,0,0,0],
[1,0,0,0,0,0],
[0,0,1,0,0,1],
[0,0,0,1,0,0],
[0,0,0,0,1,0]]
print(domino(G))