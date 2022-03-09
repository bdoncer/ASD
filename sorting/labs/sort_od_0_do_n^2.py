def CountSort(T, k,option):
    counter = [0] * k
    res = [0] * len(T)
    for i in range(len(T)):
        counter[T[i][option]] += 1
    for i in range(1, k):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[T[i][option]] -= 1
        res[counter[T[i][option]]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]
def zmiana_liczby(a,n):
    x = a//n
    y = a-x*n
    return [x,y]

def sortu_sort(A,n):
    B = [-1]*len(A)
    for i in range(len(A)):
        A[i] = zmiana_liczby(A[i],n)
    CountSort(A,n,1)
    CountSort(A,n,0)
    for i in range(len(A)):
        A[i] = n*A[i][0]+A[i][1]



A = [1,5,3,24,3,16,22,7,15,21]
sortu_sort(A,5)
print(A)