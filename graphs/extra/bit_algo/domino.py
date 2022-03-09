class Node:
    def __init__(self):
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
    y.parent = x


def domino(G,n):
    A = [Node() for _ in range(n)]
    for i in range(len(G)):
        if A[G[i][1]].parent == A[G[i][1]]:
            union(A[G[i][0]],A[G[i][1]])
    res = 0
    for i in range(n):
        if A[i].parent == A[i]:
            res += 1
    return res

G = [[0,1],[1,3],[1,2],[3,0],[4,2]]
print(domino(G,5))

