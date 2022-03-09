from math import inf
def opt_sum(T):
    n = len(T)
    F = [[inf]*n for _ in range(n)]
    S = [0]*n
    S[0] = T[0]
    for i in range(1,n):
        S[i] = S[i-1]+T[i]
    for i in range(n-1):
        F[i][i] = T[i]
        F[i][i+1] = abs(T[i]+T[i+1])
    F[n-1][n-1]=T[n-1]
    for line in F:
        print(line)
    for i in range(n):
        for j in range(i,n):
            for k in range(i,j):
                F[i][j] = min(F[i][j],min(max(F[i][k],F[k+1][j]),abs(S[j]-S[i]+T[i])))
            F[i][j] = max(F[i][j],abs(S[j]-S[i]+T[i]))

T = [2,-5,1]
opt_sum(T)