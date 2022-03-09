#index = floor(((array[i]-mini)*n)/(maxi-mini+1))
#stabilny
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



def insertion_sort(tab, a):
    for j in range(1, len(tab)):
        key = tab[j]
        i = j - 1
        while i >= 0 and log(tab[i], a) > log(key, a):
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = key


def fast_sort(tab, a):
    n = len(tab)
    b = [[] for _ in range(n)]
    for i in range(n):
        bucket = int(n * log(tab[i], a))
        if bucket == n:
            bucket = n-1
        b[bucket].append(tab[i])
    for bucket in b:
        insertion_sort(bucket, a)
    k = 0
    for i in range(n):
        for elem in b[i]:
            tab[k] = elem
            k += 1
    return tab

T = [0.12, 0.11, 0.9, 0.7,0.5,0.77,0.81,0.53]
BucketSort(T)
