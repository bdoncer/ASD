def klocki(A):
    n = len(A)
    F = [1]*n
    for i in range(1,n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
                F[i] = max(F[i],F[j]+1)
    maksik = F[0]
    for i in range(n):
        maksik = max(maksik,F[i])
    return n-maksik

A = [(4,8),(2,3),(5,7),(6,7),(1,2)]
print(klocki(A))
