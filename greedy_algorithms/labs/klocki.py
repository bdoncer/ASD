from math import inf
def klocki(A,max_waga):
    n = len(A)
    F = [[inf]*(max_waga+1) for _ in range(n)]
    F[0][A[0]] = 1
    for i in range(1,n):
        for w in range(max_waga+1):
            if A[i] > w:
                F[i][w] = F[i-1][w]
            if w-A[i]>=0:
                F[i][w] = min(F[i-1][w],F[i-1][w-A[i]]+1)
            if w == A[i]:
                F[i][w] = 1
    for k in range(max_waga,-1,-1):
        if F[n-1][k] != inf:
            return F[n-1][k]

A = [6,5,3]
print(klocki(A,8))