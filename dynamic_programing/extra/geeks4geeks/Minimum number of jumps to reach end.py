from math import inf
def jumps(A):
    F = [inf]*len(A)
    n = len(A)
    F[0] = 0
    for i in range(n):
        for j in range(1,A[i]+1):
            if i+j<n:
                F[i+j] = min(F[i+j],F[i]+1)
    return F[n-1]

print(jumps([1, 3, 6, 1, 0, 9]))
