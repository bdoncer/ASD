def problem_plecakowy(W, P, MaxWaga):
    ile_przedmiotow = len(W)
    T = [0] * ile_przedmiotow
    suma_cen = 0
    for i in range(ile_przedmiotow):
        suma_cen += P[i]
    for i in range(ile_przedmiotow):
        T[i] = [10**8] * (suma_cen + 1)
    T[0][P[0]] = W[0]
    for w in range(1,ile_przedmiotow):
        for k in range(suma_cen+1):
            T[w][k] = T[w-1][k]
            if (P[w] == k):
              T[w][k] = min(T[w][k], W[w])
            if k >= P[w]:
              T[w][k] = min(T[w][k],W[w] + T[w-1][k-P[w]])
    res = 0
    for i in range(suma_cen+1):
        if T[ile_przedmiotow-1][i] != 10**8 and T[ile_przedmiotow-1][i] <= MaxWaga:
            res = i
    print(getsolution(T,W,P,ile_przedmiotow-1,res))
    for line in T:
        print(line)
    return res


def getsolution(T, W, P, w, k):
    if w == 0:
        if P[w] <= k:
            return [0]
        else:
            return []
    if k == P[w]:
        return getsolution(T, W, P, w - 1, k - P[w]) + [w]
    if k - P[w] >= 0 and T[w][k] == T[w - 1][k - P[w]] + W[w]:
        return getsolution(T, W, P, w - 1, k - P[w]) + [w]
    return getsolution(T, W, P, w - 1, k)


ceny = [1, 2, 10]
wagi = [2, 3, 1]
print(problem_plecakowy(wagi, ceny, 4))