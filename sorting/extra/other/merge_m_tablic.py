def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):
    index = i
    if left(i) < n and A[left(i)][0] < A[i][0]:
        index = left(i)
    if right(i) < n and A[right(i)][0] < A[index][0]:
        index = right(i)
    if i != index:
        A[i], A[index] = A[index], A[i]
        heapify(A, n, index)

def buildheap(A, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def wstaw_do_kopca(A,val):
    A.append(val)
    i = len(A)-1
    while A[parent(i)][0] > val[0] and i != 0:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def merge_n_tablic(T):
    n = len(T)
    indeksy = [0]*n
    kopiec = []
    wynik = []
    for i in range(n):
        k = [T[i][0],i]
        wstaw_do_kopca(kopiec,k)
    while len(kopiec) != 0:
        wynik.append(kopiec[0][0])
        print(wynik)
        skad = kopiec[0]
        indeksy[skad[1]] += 1
        if indeksy[skad[1]] < len(T[skad[1]]):
            kopiec[0] = [T[skad[1]][indeksy[skad[1]]],skad[1]]
            heapify(kopiec,len(kopiec),0)
        else:
            del kopiec[0]
            heapify(kopiec,len(kopiec),0)

T = [[ 15,20,34,45,67,89 ],
[ 10,15,23,45,78,789],
[ 27 ],
[ 32 ]]
merge_n_tablic(T)
