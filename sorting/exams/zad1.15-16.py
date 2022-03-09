def partition(T, left, right):
    pivot = T[right][0]
    border = left - 1
    for i in range(left, right + 1):
        if T[i][0] < pivot:
            border += 1
            if border != i:
                T[i], T[border] = T[border], T[i]

    if border + 1 != right:
        T[border + 1], T[right] = T[right], T[border + 1]
    return border


def sort(T, left, right):
    while left < right:
        border = partition(T, left, right)
        if border - left + 1 < right - border - 1:
            sort(T, left, border)
            left = border + 2
        else:
            sort(T, border + 2, right)
            right = border


def sum(A, B, n):
    sumy = [0] * n
    tuple = []
    for i in range(n ** 2):
        sumy[i // n] += A[i]
    for i in range(n):
        tuple.append((sumy[i],i))
    sort(tuple, 0, n - 1)
    k = 0
    j = 0
    while k < n:
        index = n*tuple[k][1]
        for i in range(index,index+n):
            B[j] = A[i]
            j += 1
        k += 1
    print(tuple)




A = [4, 7, 3, 6, 7, 3, 5, 77, 8, 33, 4, 5, 77, 8, 3, 33, 4, 6, 44, 6, 55, 8, 3, 6, 23]
B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum(A, B, 5)
print(A)
print(B)