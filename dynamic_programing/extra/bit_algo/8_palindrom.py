def najdluzszy_palindrom(A):
    n = len(A)
    F = [[False]*n for _ in range(n)]
    for i in range(n):
        F[i][i] = True
    for i in range(n-1):
        if A[i] == A[i+1]:
            F[i][i+1] = True
    for i in range(2,n):
        for j in range(n-i):
                F[i][j+i] = F[i+1][j+i-1] and A[i] == A[i+j]
    max_len = 0
    for i in range(n):
        for j in range(n):
            if F[i][j] == True and abs(i-j)+1>max_len:
                max_len = abs(i-j)+1
    for line in F:
        print(line)
    return max_len

A = ['c','a','c','a','c']
print(najdluzszy_palindrom(A))


