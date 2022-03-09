def plecak(W,P,max_waga,min_cena):
    n = len(W)
    suma_cen = 0
    for i in range(n):
        suma_cen += P[i]
    F = [[[0]*(suma_cen+1) for _ in range(max_waga+1)] for _ in range(n)]
    F[0][W[0]][P[0]] = 1
    for i in range(1,n):
        for j in range(max_waga+1):
            for k in range(suma_cen+1):
                F[i][j][k] = F[i-1][j][k]
                if W[i] == j and P[i] == k:
                    F[i][j][k] += 1
                if j-W[i] >= 0 and k-P[i] >= 0:
                    F[i][j][k] += F[i-1][j-W[i]][k-P[i]]
    for cell in F:
        print("")
        for line in cell:
            print(line)
    res = 0
    for j in range(max_waga+1):
        for k in range(min_cena,suma_cen+1):
            res += F[n-1][j][k]
    print(res)

P = [1,2,3]
W = [1,2,1]

print(plecak(W,P,1,0))

