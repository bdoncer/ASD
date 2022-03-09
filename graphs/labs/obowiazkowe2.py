def czy_istnieje(T, suma):
    n = len(T)
    W = [0] * n
    for i in range(n):
        W[i] = [0] * (suma + 1)
    W[0][0] = 1
    W[0][T[0]] = 1
    for w in range(n):
        for k in range(suma + 1):
            if W[w - 1][k] == 1:
                W[w][k] = 1
                if k + T[w] <= suma:
                    W[w][k + T[w]] = 1
            if k == suma and W[w][k] == 1:
                for line in W:
                    print(line)
                print(print_solution(T, W, w, k))
                return True
    return False


def print_solution(T, W, w, k):
    if w == 0:
        if W[0][k] == 1 and k!=0:
            return [0]
        else:
            return []

    if W[w - 1][k] == 1:
        return print_solution(T, W, w - 1, k)
    else:
        return print_solution(T, W, w - 1, k - T[w]) + [w]


T = [2, 8, 1, 3, 7, 9]
print(czy_istnieje(T, 19))
