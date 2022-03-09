def gdzie_mosty(G):
    time = 1
    def DFS_visit(G, i):
        nonlocal time
        visited[i] = True
        for neigh in G[i]:
            if neigh == parent[i]:
                continue
            if visited[neigh] == False:
                parent[neigh] = i
                times[neigh] = time
                low[neigh] = time
                time += 1
                DFS_visit(G, neigh)
            else:
                low[i] = min(low[i],times[neigh])
                w = parent[i]
                while w != None and low[w] > low[i]:
                    low[w] = low[i]
                    w = parent[w]
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    times = [-1]*n
    low = [-1]*n
    times[0]=0
    low[0]=0
    for i in range(n):
        if visited[i] == False:
            DFS_visit(G, i)
    mosty = []
    for i in range(n):
        if times[i] == low[i] and parent[i] != None:
            mosty.append([i,parent[i]])
    return mosty

def DFS(G,C,i):
    sum = C[i]
    def DFS_visit2(G,C,i):
        nonlocal sum
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                sum += C[neigh]
                DFS_visit2(G,C, neigh)
    n = len(G)
    visited = [False]*n
    DFS_visit2(G,C,i)
    return sum

from queue import Queue
def BFS(G,C,mosty,s):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    visited[s] = True
    Q.put(s)
    suma_max = 0
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            if visited[neigh] == False:
                visited[neigh] = True
                Q.put(neigh)
                s,e = czy_most(mosty,neigh)
                if s != -1:
                    usun_krawedz(G,s,e)
                    suma = DFS(G,C,e)
                    if suma > suma_max:
                        suma_max = suma
    return suma_max

def usun_krawedz(G,s,e): #z e do s
    for i in range(len(G[e])):
        if G[e][i] == s:
            G[e].pop(i)
            break
    for i in range(len(G[s])):
        if G[s][i] == e:
            G[s].pop(i)
            break

def czy_most(mosty,i):
    for k in range(len(mosty)):
        if mosty[k][0] == i:
            return mosty[k][0],mosty[k][1]
        if mosty[k][1] == i:
            return mosty[k][1],mosty[k][0]
    return [-1,-1]

def myjestesmykrasnoludki(G,C,kryjowka):
    mosty = gdzie_mosty(G)
    return BFS(G,C,mosty,kryjowka)


_G = [
    [1, 2],
    [0, 2],
    [1, 0, 3],
    [2, 4],
    [3, 5, 6, 7],
    [4, 7, 6],
    [4, 5, 7],
    [4, 5, 6, 8],
    [7, 9, 10, 11],
    [8, 11],
    [8, 11],
    [8, 9, 10]
]
# Kryjówka na 6 indexie
trolls = [100, 5, 6, 2, 1, 3, 0, 100, 15, 1, 3, 2]
print(myjestesmykrasnoludki(_G,trolls,6))