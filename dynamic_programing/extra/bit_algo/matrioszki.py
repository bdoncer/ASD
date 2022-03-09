def matrioszki(T):
    F = [1]*len(T)
    n = len(T)
    T.sort()
    for i in range(1,n):
        for k in range(i):
            if T[i][1] > T[k][1] and T[i][0] > T[k][0]:
                F[i] = max(F[i],F[k]+1)
    print(F)
    res = 0
    for i in range(n):
        res = max(res,F[i])
    return res

T = [[2, 4], [1, 3], [2, 3], [4, 10]]
print(matrioszki(T))