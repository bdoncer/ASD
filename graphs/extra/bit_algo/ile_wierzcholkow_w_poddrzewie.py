def wierzcholki(G,T,v):
    res = 1
    if len(G[v])== 0:
        T[v] = 1
        return 1
    for neigh in G[v]:
        res += wierzcholki(G,T,neigh)
    T[v] = res
    return res
T = [0,0,0,0,0,0,0,0]
G = [[1,2,3],[4,5,6],[7],[],[],[],[],[]]
wierzcholki(G,T,0)
print(T)