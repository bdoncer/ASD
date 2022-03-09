from math import inf
def bob(A,x):
    n = len(A)
    A = sorted(A, key=lambda x: x[1])
    print(A)
    F = [[inf]*(n) for _ in range(n+1)]
    for i in range(n):
        F[1][i] = 0
    for i in range(2,n+1):
        for j in range(i-1,n):
            for k in range(0,j):
                if A[j][0]-A[k][1] >= 0:
                    F[i][j] = min(F[i][j],F[i-1][k]+A[j][0]-A[k][1])
    res = inf
    for i in range(n):
        res = min(res,F[x][i])
    return res

def bob_2(A,k):
    n = len(A)
    A = sorted(A, key=lambda x: x[1])
    print(A)
    F = [[inf] * (k+1) for _ in range(n)]
    for i in range(n):
        F[i][0] = 0
        F[i][1] = 0
    for i in range(1, n):
        for j in range(2,i+2):
            if j < k+1:
                for p in range(j-2, i):
                    if A[i][0] - A[p][1] >= 0:
                        F[i][j] = min(F[i][j], F[p][j-1] + A[i][0] - A[p][1])
    res = inf
    for i in range(n):
        res = min(res, F[i][k])
    return res



A = [(2,3),(4,7),(3.5,10)]
print(bob(A,2))
print(bob_2(A,2))