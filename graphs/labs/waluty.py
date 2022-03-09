from math import inf,log2
def Bellman_Ford(G,s,t):
    n = len(G)
    d = [inf]*n
    parent = [None]*n
    d[s] = 0
    for i in range(n-1):
        for j in range(n):
            for edge in G[j]:
                neigh = edge[0]
                weigh = edge[1]
                weigh = log2(weigh)
                if d[neigh] > d[j] + weigh:
                    d[neigh] = d[j] + weigh
                    parent[neigh] = j
    #czy jest ujemny cykl
    for j in range(n):
        for edge in G[j]:
            neigh = edge[0]
            weigh = edge[1]
            weigh = log2(weigh)
            if d[neigh] > d[j] + weigh:
                return "cykl tiririri"
    return d[t]


_G = [
    [[1, 5], [2, 2]],
    [[3, 1]],
    [[1, 1], [4, 2]],
    [[5, 3], [4, 1]],
    [[5, 2], [2, 0.5]],
    []
]
print(Bellman_Ford(_G,0,5))