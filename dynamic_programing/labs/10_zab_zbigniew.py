from math import inf
def jump(A):
    n = len(A)
    max_energy = 0
    for i in range(n):
        max_energy += A[i]
    F = [[inf]*max_energy for _ in range(n)]
    F[0][A[0]] = 0
    for i in range(1,n):
        for j in range(max_energy):
            for k in range(1,i+1):
                if j+k-A[i] >= 0 and j+k-A[i] < max_energy and F[i-k][j+k-A[i]] != inf:
                    F[i][j] = min(F[i][j],F[i-k][j+k-A[i]])+1
    res = inf
    for i in range(max_energy):
        if F[n-1][i] < res:
            res = F[n-1][i]
    return res

A = [3,1,1,5]
print(jump(A))