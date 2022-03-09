def problem_plecakowy(W, P, MaxWaga):
    ile_przedmiotow = len(W)
    T = [0] * ile_przedmiotow
    for i in range(ile_przedmiotow):
        T[i] = [0] * (MaxWaga + 1)
    for i in range(W[0], MaxWaga + 1):
        T[0][i] = P[0]
    for p in range(ile_przedmiotow):
        for w in range(MaxWaga + 1):
            T[p][w] = T[p - 1][w]
            if w - W[p] >= 0:
                T[p][w] = max(T[p - 1][w], T[p - 1][w - W[p]] + P[p])
    res = getsolution(T, W, P, ile_przedmiotow - 1, MaxWaga)
    print(res)
    return T[ile_przedmiotow-1][MaxWaga]


def getsolution(T, W, P, p, w):
    if p == 0:
        if w >= 0 and T[0][w] == P[0]:
            return [0]
        else:
            return []
    if w - W[p] >= 0 and T[p][w] == T[p - 1][w - W[p]] + P[p]:
        return getsolution(T, W, P, p - 1, w - W[p]) + [p]
    return getsolution(T, W, P, p - 1, w)


wagi = [2, 2, 3, 15, 1, 4, 5, 6]
rzeczy = [40, 160, 70, 300, 70, 25, 25, 180]
print(problem_plecakowy(wagi, rzeczy, 15))
