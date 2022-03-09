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
    G = sorted(G,key=lambda x:x[2])
    T = [Node(i) for i in range(wierzcholki)]
    print(G)
    res = 0
    for i in range(len(G)):
        w1 = G[i][0]
        w2 = G[i][1]
        weigh = G[i][2]
        if find(T[w1]) != find(T[w2]):
            if weigh > res:
                res = weigh
            union(T[w1],T[w2])
            print(w1,w2)
    return res
from math import sqrt
def odl_euklidesowa(x1,y1,x2,y2):
    return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
def arktyczna_siec(G,P):
    F = []
    n = len(P)
    '''for i in range(n-1):
        if P[i] == 1:
            for j in range(i+1,n):
                if P[j] == 1:
                    F.append((i,j,0))'''
    for i in range(n-1):
        for j in range(i+1,n):
            if P[i] == 1 and P[j] == 1:
                F.append((i,j,0))
            else:
                F.append((i,j,odl_euklidesowa(G[i][0],G[i][1],G[j][0],G[j][1])))
    return Kruskal(F,n)

G = [
    (0,0),
    (4,0),
    (8,0),
    (8,3),
    (4,3),
    (0,3)]
P = [0,1,0,1,0,1]
print(arktyczna_siec(G,P))

