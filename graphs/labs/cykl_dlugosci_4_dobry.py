def cykl(G):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if i != j:
                res = []
                for k in range(n):
                    if G[i][k] == 1 and G[j][k] == 1:
                        res.append(k)
                    if len(res) == 2:
                        res.append(i)
                        res.append(j)
                        return res
    return False

G= [[0,1,0,0,0,0],[0,0,0,1,0,1],[0,0,0,1,0,0],[0,1,1,0,1,0],[0,0,0,1,0,1],[0,1,0,0,1,0]]
print(cykl(G))