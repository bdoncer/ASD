def sciezki(G,v,s,t):
    res = 0
    if v == t:
        return 1
    for neigh in G[v]:
        res += sciezki(G,neigh,s,t)
    return res






G= [[1,2],[2,3],[3],[]]
print(sciezki(G,1,1,3))
