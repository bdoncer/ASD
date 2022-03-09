from math import inf
def znajdz_mosty(G):
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
    mosty = []
    for i in range(len(G)):
        if time_o[i] == low[i] and parent[i] != None:
            mosty.append([i, parent[i]])

    return mosty
def czy_most(v,mosty):
    for most in mosty:
        if v==most[0] or v==most[1]:
            return most
    return -1

def DFS_licz(G,v,visited,values):
    wynik = 0
    def DFS_licz_visit(G,v,visited,values):
        nonlocal wynik
        visited[v] = True
        wynik += values[v]
        for neigh in G[v]:
            if visited[neigh] == False:
                visited[neigh] = True
                DFS_licz_visit(G, neigh,visited,values)
    DFS_licz_visit(G,v,visited,values)
    return wynik


def DFS_lista(G,mosty,visited,values,s):
    best = 0
    def DFS_visit(G,v):
        nonlocal best
        visited[v] = True
        if czy_most(v,mosty) != -1:
            res = czy_most(v,mosty)
            if v ==res[0]:
                val = DFS_licz(G,res[1],visited,values)
            else:
                val = DFS_licz(G,res[0],visited,values)
            if val > best:
                best = val

        for neigh in G[v]:
            if visited[neigh] == False:
                DFS_visit(G,neigh)

    DFS_visit(G,s)
    return best


def krasnoludki(G,values,s):
    mosty = znajdz_mosty(G)
    visited = [False] * len(G)
    return DFS_lista(G,mosty,visited,values,s)

G = [[1,2],[0,2],[0,1,3],[2,4,5],[3,5],[3,4,6],[5,7,8],[6,8],[6,7,9],[8]]
values = [3,2,8,4,3,1,0,8,10,10000]
#graf = [[1, 6], [0, 2], [1, 3, 6], [2, 4, 5], [3, 5], [3, 4], [0, 2, 7], [6]]
print(krasnoludki(G,values,0))