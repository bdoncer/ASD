def max_sciezka(G,T,P,v=0):
    if len(G[v]) == 0:
        T[v] = P[v]
        return P[v]
    res = 0
    for neigh in G[v]:
        res = max(res,max_sciezka(G,T,P,neigh))
    T[v] = res+P[v]
    return T[v]
def rozwiaznie(T,G):
    res = 0
    for i in range(len(T)):
        best1=0
        best2=0
        for v in G[i]:
            if T[v] > best1:
                best2 = best1
                best1= T[v]
            elif T[v] > best2:
                best2 = T[v]
        temp_res = max(best1,best1+best2+T[i])
        if temp_res > res:
            res = temp_res
    return res


G = [[1,2,3],[4],[],[5,6,7,8],[9,10],[],[],[],[],[],[]]
P = [7,1,-8,-4,-2,2,1,8,-2,5,-2]
T = [0,0,0,0,0,0,0,0,0,0,0]

max_sciezka(G,T,P)
print(T)

print(rozwiaznie(T,G))
