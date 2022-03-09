def rownanie(mnozniki, res):
    n = len(mnozniki)
    T = [0] * (res + 1)
    T[0] = 1
    for i in range(n):
        minimal = mnozniki[i]
        for j in range(minimal, res + 1):
            T[j] += T[j - mnozniki[i]]
    print(T)
    return T[res]



mnozniki = [1, 3, 5, 7]
res = 8
print(rownanie(mnozniki,res))
































'''def count(coeff, rhs):
 
    k = len(coeff)
 
    T = [[0] * (rhs + 1) for _ in range(k + 1)]
 
    for i in range(k + 1):
        T[i][0] = 1
 
    for i in range(1, k + 1):
        for j in range(1, rhs + 1):
            if coeff[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i][j - coeff[i - 1]]
 
    return T[k][rhs]'''


