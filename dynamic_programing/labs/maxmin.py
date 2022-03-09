def maxmin(A,k):
    n = len(A)
    F = [[0]*(k+1) for _ in range(n)]
    prefix = [0]*n
    prefix[0] = A[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1]+A[i]
    for i in range(n):
        F[i][1] = prefix[i]
    F[0][1] = A[0]
    for i in range(n):
        for j in range(k+1):
            for t in range(1,i-j+2):
                F[i][j] = max(F[i][j],min(F[i-t][j-1],prefix[i]-prefix[i-t-1]))
    return F[n-1][k]

A = [2,1,3,1,1,5]
print(maxmin(A,3))
