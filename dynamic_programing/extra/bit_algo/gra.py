from math import inf
def gra(A):
    n = len(A)
    F = [[inf]*n for _ in range(n)]
    for i in range(n):
        F[i][i] = A[i]
    for i in range(n-1):
        F[i][i+1] = max(A[i],A[i+1])
    return rec(A,F,0,len(A)-1)
def rec(A,F,i,j):
    if F[i][j] != inf:
        return F[i][j]
    F[i][j] = max(A[i]+min(rec(A,F,i+2,j),rec(A,F,i+1,j-1)),A[j]+min(rec(A,F,i,j-2),rec(A,F,i+1,j-1)))
    return F[i][j]

def mentoski(T, n, help):
    pref = [i for i in T]
    for i in range(n):
        help[i][i] = T[i]
        if i > 0:
            pref[i] += pref[i-1]
    for el in help:
        print(el)
    for l in range(2, n):
        for m in range(n-l):
            help[m][m+l] = pref[m+l] - pref[m]
            help[m][m+l] -= min(help[m-l][m+l], help[m][m+l-1])
    return help[0][n-1]

T = [5,3,6,3,6]
print(gra(T))
