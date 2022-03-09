def podciag(A,B):
    n= len(A)
    m = len(B)
    F = [[0]*m for _ in range(n)]
    for i in range(m):
        if A[0] == B[i]:
            for j in range(i,m):
                F[0][j] = 1
            break
    for i in range(n):
        if B[0] == A[i]:
            for j in range(i,n):
                F[j][0] = 1
            break
    for i in range(1,n):
        for j in range(1,m):
            if A[i] == B[j]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max(F[i-1][j],F[i][j-1])
    for line in F:
        print(line)
    print_solutio(A,B,F,n-1,m-1,F[n-1][m-1])

def print_solutio(A,B,F,i,j,res,ctr = 0):
    if ctr == res:
        return
    if A[i] == B[j]:
        print(A[i])
        print_solutio(A,B,F,i-1,j-1,res,ctr+1)
    else:
        if F[i][j] == F[i-1][j]:
            print_solutio(A,B,F,i-1,j,res,ctr)
        else:
            print_solutio(A, B, F, i, j-1,res,ctr)



A = [1,1,1,3,67,4,7,43,4,8,2]
B = [1,4,8,3,1,67,5,8,4]
print(podciag(A,B))

