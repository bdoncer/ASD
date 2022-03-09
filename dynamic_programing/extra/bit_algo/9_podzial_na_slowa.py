def dict(p,k,slowa):
    a = T[p:k+1]
    for i in range(len(slowa)):
        if slowa[i] == a:
            return True
    return False

def podzial(A):
    n = len(A)
    F = [[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            F[i][j] = dict(i, j, slowa)
            for k in range(i,j):
                F[i][j] = F[i][j] or (F[i][k] and F[k+1][j])
    for line in F:
        print(line)
    print(F[0][n-1])
slowa = ["a", "pa"]
T = "apaaaaa"
podzial(T)
