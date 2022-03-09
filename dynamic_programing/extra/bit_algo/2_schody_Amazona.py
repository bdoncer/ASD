def ile_sposobow(A, T, index):
    for i in range(index):
        if index - i <= A[i]:
            T[index] += T[i]


def skok(A):
    n = len(A)
    T = [0] * n
    T[0] = 1
    for i in range(1, n):
        ile_sposobow(A, T, i)
    print(T)
    return T[n - 1]


arr = [1, 3,2 ,2, 1, 0]
print(skok(arr))
