def partition(T, l, r,option):
    pivot = T[r][option]
    i = l - 1
    for j in range(l, r):
        if T[j][option] >= pivot:
            i = i + 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1

def QuickSort(T, l, r,option):
    if l < r:
        i = partition(T, l, r,option)
        QuickSort(T, l, i - 1,option)
        QuickSort(T, i + 1, r,option)

from math import floor
def binary_search(T, x,y):
    l = 0
    r = len(T) - 1
    while l <= r:
        m = floor((l + r) / 2)
        if T[m][0] == x and T[m][1] == y:
            return m
        if T[m][1] > y:
            r = m - 1
        elif T[m][1] < y:
            l = m + 1
    return None
def dominowanie(X):
    n = len(X)
    Y = [-1]*n
    for i in range(n):
        Y[i] = X[i]
    QuickSort(X,0,n-1,0)
    QuickSort(Y, 0, n-1, 1)
    ctr = 0
    skreslone = 0
    ind = 0
    while skreslone != n:
        x = X[ind][0]
        y = X[ind][1]
        for i in range(n):
            if Y[i][0] == x and Y[i][1] == y:
                skad

        for i in range(k,n):




T = [(5,2),(2,1),(4,3),(1,5)]
dominowanie(T)