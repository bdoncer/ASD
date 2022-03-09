'''zad. 3 (najdłuższy wspólny podciąg) - Mamy dane dwie tablice,
  A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu.'''

def najdluzszy(A,B):
    n = len(A)
    m = len(B)
    F = [[0]*(m+1) for _ in range(n+1)]
    F[0][m] = 0
    F[n][0] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    for line in F:
        print(line)
    return F[n][m]

A = [2,1,3]
B = [1,2,1]
print(najdluzszy(A,B))