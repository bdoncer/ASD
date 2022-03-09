def bagaze(T):
    n = len(T)
    waga = 0
    for i in range(n):
        waga += T[i]
    if waga%2 == 1:
        return False
    waga = waga//2
    F = [[False]*(waga+1) for _ in range(n)]
    F[0][T[0]] = True
    for i in range(1,n):
        for j in range(waga+1):
            F[i][j] = F[i-1][j]
            if j-T[i]>0:
                F[i][j] = F[i][j] or F[i-1][j-T[i]]
            if j == T[i]:
                F[i][j] = True
    for i in range(n):
        if F[i][waga] == True:
            index = i
            break
    print(index)
    suma = waga
    suma -= T[index]
    while suma != 0:
        if F[index-1][suma] == True:
            index -= 1
            suma -= T[index]
            print(index)


T = [1,1,2,2]
bagaze(T)
