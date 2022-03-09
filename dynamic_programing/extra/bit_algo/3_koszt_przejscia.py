def przejscie(W):
    M = len(W)
    N = len(W[0])
    T = [0] * M
    for i in range(M):
        T[i] = [0] * N
    T[0][0] = W[0][0]
    for i in range(1, N):
        T[0][i] = T[0][i - 1] + W[0][i]
    for i in range(1, M):
        T[i][0] = T[i - 1][0] + W[i][0]

    for w in range(1,M):
        for k in range(1,N):
            T[w][k] = min(T[w-1][k],T[w][k-1]) + W[w][k]
    print(print_wynik(W,T,M-1,N-1))
    return T[M-1][N-1]

def print_wynik(W,T,M,N):
    if M==0 and N==0:
        return [W[M][N]]
    if M > 0 and T[M][N] == T[M-1][N] + W[M][N]:
        return print_wynik(W,T,M-1,N)+[W[M][N]]
    if N > 0 and T[M][N] == T[M][N-1] + W[M][N]:
        return print_wynik(W,T,M,N-1)+[W[M][N]]



arr = [
    [3, 1, 4, 2, 3, 1, 7],
    [2, 4, 5, 2, 1, 4, 2],
    [3, 1, 5, 4, 2, 3, 1],
    [4, 1, 7, 3, 4, 1, 1],
    [1, 2, 3, 7, 3, 4, 1],
    [1, 2, 4, 2, 2, 7, 2],
    [3, 4, 1, 3, 1, 4, 1]
]
_arr = [
    [3, 1, 1, 1, 1, 1, 1],
    [2, 4, 5, 2, 1, 4, 1],
    [3, 1, 5, 4, 2, 3, 1],
    [4, 1, 7, 3, 4, 1, 1],
    [1, 2, 3, 7, 3, 4, 1],
    [1, 2, 4, 2, 2, 7, 1],
    [3, 4, 1, 3, 1, 4, 1]
]

__arr = [
    [3, 1, 1, 1, 1, 1, 1],
    [2, 4, 5, 2, 1, 4, 1],
    [3, 1, 5, 4, 2, 3, 1],
    [4, 1, 7, 3, 4, 1, 1],
    [1, 2, 3, 7, 3, 4, 1],
    [1000000, 2, 4, 2, 2, 7, 1],
    [0, 0, 0, 0, 0, 0, 1]
]
print(przejscie(__arr))
