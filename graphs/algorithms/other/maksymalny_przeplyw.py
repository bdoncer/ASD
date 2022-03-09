#(V+E)*max_p (EK VE2)
from math import inf
def DFS(G,s):
    minimum = inf
    def DFS_visit(G, i):
        nonlocal minimum
        visited[i] = True
        for j in range(len(G[i])):
            neigh = j
            waga = G[i][j]
            if waga != 0 and visited[neigh] == False:
                parent[neigh] = i
                if waga < minimum:
                    minimum = waga
                DFS_visit(G, neigh)

    n = len(G)
    visited = [False]*n
    parent = [None]*n
    DFS_visit(G,s)
    return visited,parent,minimum
def Ford_Fulkerson(G,s,t): #na macierzy
    #robie dowolny przeplyw
    res = 0
    while True:
        visited,parent, minimum = DFS(G, s)
        if visited[t] == False:
            break
        res += minimum
        index = t
        while index != s:
            G[index][parent[index]] += minimum
            G[parent[index]][index] -= minimum
            index = parent[index]
    return res

_G1 = [
    [0, 7, 5, 0, 0, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 10, 0],
    [0, 0, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0],
]
print(Ford_Fulkerson(_G1,0,5))

