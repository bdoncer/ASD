#V*E
from math import inf
def Bellman_Ford(G,s):
    n = len(G)
    d = [inf]*n
    parent = [None]*n
    d[s] = 0
    for i in range(n-1):
        for j in range(n):
            for edge in G[j]:
                neigh = edge[0]
                weigh = edge[1]
                if d[neigh] > d[j] + weigh:
                    d[neigh] = d[j] + weigh
                    parent[neigh] = j
    #czy jest ujemny cykl
    for j in range(n):
        for edge in G[j]:
            neigh = edge[0]
            weigh = edge[1]
            if d[neigh] > d[j] + weigh:
                return "ujemny cykl bro"
    return d



_G = [
    [[1, 1], [2, 1]],
    [[2, 1], [6, -2]],
    [[5, 1], [3, 2]],
    [[4, -2]],
    [[5, -2]],
    [[7, 1]],
    [[8, 5]],
    [[6, 1], [8, 1]],
    []
]
_GG = [[[1,1]],[[2,2]],[[0,-4]]]
print(Bellman_Ford(_GG,0))