def common_podciag(A,B):
    n = len(A)
    m = len(B)
    F = [[0]*n for _ in range(m)]
    for i in range(m):
        if A[0] == B[i]:
            F[i][0] = 1
    for j in range(n):
        if A[j] == B[0]:
            F[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            if B[i] == A[j]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    return F[m-1][n-1]

def common_po_kolei(A,B):

    n = len(A)
    m = len(B)
    F = [[0] * n for _ in range(m)]
    for i in range(m):
        if A[0] == B[i]:
            F[i][0] = 1
    for j in range(n):
        if A[j] == B[0]:
            F[0][j] = 1
    res = 0
    for i in range(1, m):
        for j in range(1, n):
            if B[i] == A[j]:
                F[i][j] = F[i - 1][j - 1] + 1
                if F[i][j] > res:
                    res = F[i][j]
    return res

A = [8,7,6]
B=[5,8,7,4,6,3]

print(common_podciag(A,B))
print(common_po_kolei(A,B))
