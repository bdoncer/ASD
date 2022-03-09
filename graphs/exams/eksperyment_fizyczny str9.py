from math import floor
def InsertSort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while key < T[j] and j >= 0:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

def BucketSort(T):
    n = len(T)
    # tworze n kubelkow
    # rozmiar kubelka 1/n
    # indeks kubelka floor(A[i]*n)
    A = [[] for _ in range(n)]
    for i in range(n):
        index = floor(T[i] * n)
        A[index].append(T[i])
    for i in range(len(A)):
        if len(A[i]) > 0:
            InsertSort(A[i])
    i = 0
    j = 0
    index = 0
    while index < len(T):
        if j < len(A[i]):
            T[index] = A[i][j]
            j += 1
            index += 1
        else:
            j = 0
            i += 1

def fast_sort(T,a):
    BucketSort(T)
    for i in range(len(T)):
        T[i] = pow(a,T[i])
    return T
T = [0.1,0.3,0.25,0.5,0.75,0.9]
print(fast_sort(T,2))
