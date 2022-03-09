'''2. Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
dlog ne elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.'''

from random import randint, seed
from math import log2, ceil, floor

def partition(T,left,right):
    pivot = T[right]
    border = left - 1
    for i in range(left,right+1):
        if T[i] < pivot:
            border += 1
            if border != i:
                T[i],T[border] = T[border],T[i]

    if border + 1 != right:
        T[border+1],T[right] = T[right],T[border+1]
    return border

def sort(T,left,right):
    while left < right:
        border = partition(T,left,right)
        if border - left + 1 < right - border - 1:
            sort(T,left,border)
            left = border + 2
        else:
            sort(T, border + 2, right)
            right = border

def QuickSort(T):
    sort(T,0,len(T)-1)

def merge(T1,T2,res):
    i = 0
    j = 0
    ctr = 0
    while i<len(T1) and j<len(T2):
        if T1[i] < T2[j]:
            if T1[i] != -1:
                res[ctr] = T1[i]
                ctr += 1
            i += 1
        else:
            res[ctr] = T2[j]
            j += 1
            ctr += 1
    if i == len(T1):
        while j<len(T2):
            res[ctr] = T2[j]
            j += 1
            ctr += 1
    else:
        while i<len(T1):
            if T1[i] != -1:
                res[ctr] = T1[i]
                ctr += 1
            i += 1

def funkcja(A):
    n = len(A)
    parzyste = [0] * ceil(log2(n))
    ctr = 0
    for i in range(n):
        if A[i] % 2 == 0:
            parzyste[ctr] = A[i]
            ctr += 1
            A[i] = -1
    QuickSort(parzyste)
    res = [0]*n
    merge(A,parzyste,res)
    return res




seed(420)
n = 1000
arr = [randint(0, n // 2) * 2  + 1for _ in range(n)]
arr = sorted(arr)
for i in range(ceil(log2(n))):
    arr[i*floor(log2(n))] = randint(0, (n // 2)) * 2
print(arr)
print(funkcja(arr))