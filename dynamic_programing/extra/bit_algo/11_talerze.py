def talerze(T,goscie):
    N = len(T)
    for i in range(N):
        for j in range(1,N):
            T[i][j] += T[i][j-1]
    F = [[-1]*N for _ in range(goscie)]
    for i in range(goscie):
        if i < N:
            F[i][0] = T[0][i]
        else:
            F[i][0] = T[0][-1]
    for i in range(1, N):
        F[0][i] = max(F[0][i-1], T[i][0])

    for i in range(goscie): #ilu gosci
        for j in range(N): #ile stosow
            F[i][j] = ceramika(i,j,T,F)
    print(F)
    return F[goscie-1][N-1]

def ceramika(i,j,T,F):
    if F[i][j] != -1:
        return F[i][j]
    best = -1
    for k in range(len(T[0])+1):
        if k == 0:
            best = max(best, F[i][j - 1])
        else:
            if i - k >= 0:
                best = max(best, F[i - k][j - 1] + T[j][k - 1])
    return best

T = [[1,10,5],[5,1,3],[1,6,10]]
talerze(T,9)