from math import floor


def InsertSort(T):
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while key < T[j] and j >= 0:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

from math import sqrt
def BucketSort(T,k):
    n = len(T)
    # tworze n kubelkow
    # rozmiar kubelka 1/n
    # indeks kubelka floor(A[i]*n)
    A = [[] for _ in range(n)]
    r = k // sqrt(n)
    for i in range(n):
        index = floor((T[i]//r)**2)
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


A = [1,4,2,3,5,7,7,12,53,16]
BucketSort(A,53)
print(A)