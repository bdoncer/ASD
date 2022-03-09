#ElogE
class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent =self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank  > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G,wierzcholki):
    #1.Posortuj krawędzie po wagach.
    G = sorted(G,key=lambda x:x[2])
    T = [Node(i) for i in range(wierzcholki)]
    for i in range(len(G)):
        w1 = G[i][0]
        w2 = G[i][1]
        if find(T[w1]) != find(T[w2]):
            union(T[w1],T[w2])
            print(T[w1].val,T[w2].val)



G = [
    (0, 5, 1),
    (0, 2, 4),
    (0, 1, 12),
    (0, 4, 8),
    (5, 4, 7),
    (4, 3, 2),
    (3, 2, 5),
    (4, 1, 3),
    (1, 2, 6)
]
Kruskal(G,6)