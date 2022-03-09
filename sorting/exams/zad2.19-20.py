'''[2pkt.] Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''


def partition(T, left, right): #O(right-left)
    pivot = T[right]
    border = left - 1
    for i in range(right - left + 1):
        if T[i] > pivot:
            border += 1
            T[i], T[border] = T[border], T[i]
    border += 1
    T[right], T[border] = T[border], T[right]
    return border


def select(A, x, start, end): #O(n)
    if start == end:
        return A[start]
    i = partition(A, start, end)
    if i == x:
        return A[i]
    elif i > x:
        return select(A, x, start, i - 1)
    else:
        return select(A, x, i + 1, end)

def section(T,p,q): #O(n)
    p_val = select(T,p,0,len(T)-1)
    q_val = select(T, q, 0, len(T) - 1)
    res = [0]*(q-p+1)
    ctr = 0
    for i in range(len(T)):
        if T[i] <= p_val and T[i] >= q_val:
            res[ctr] = T[i]
            ctr += 1
    return res

T = [165,156,163,164,178,196,179,159]
print(section(T,2,4))
T = sorted(T)
T.reverse()
print(T)
'''def CountSort(T,k):
    counter = [0] * k
    res = [0] * len(T)
    for i in range(len(T)):
        counter[T[i]] += 1
    for i in range(1, k):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[T[i]] -= 1
        res[len(T)-counter[T[i]]-1] = T[i]
    for i in range(len(T)):
        T[i] = res[i]

def section(T,p,q):
    A = [0]*(q-p+1)
    CountSort(A,220)
    ind = 0
    for i in range(p,q+1):
        A[ind] = T[i]
        ind += 1
    return A

T = [3,5,3,7,3,4,5,6,9,2]
CountSort(T,10)
print(T)

print(section(T,2,6))'''
