#V3
from math import inf
def Floyd_Warshall(G,a,b):
    n = len(G)
    F = [[inf]*n for _ in range(n)]
    P = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                F[i][j] = G[i][j]
                P[i][j] = i
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if F[i][j] > F[i][t]+F[t][j]:
                    F[i][j] = F[i][t] + F[t][j]
                    P[i][j] = P[t][j]
    for line in F:
        print(line)
    path = [b]
    while b != a:
        path.append(P[a][b])
        b = P[a][b]
    print(path)




_G = [
    [0, -5, -1],
    [-1, 0, -1],
    [-1, -1, 0],

]
print(Floyd_Warshall(_G,0,0))