def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):
    index = i
    if left(i) < n and A[left(i)] > A[i]:
        index = left(i)
    if right(i) < n and A[right(i)] > A[index]:
        index = right(i)
    if i != index:
        A[i], A[index] = A[index], A[i]
        heapify(A, n, index)

def buildheap(A, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)
def hyhy(T,x):
    ile = 0
    def czy_wiekszy(T,x,i):
        nonlocal ile
        if i < len(T) and T[i] > x:
            ile += 1
            czy_wiekszy(T,x,left(i))
            czy_wiekszy(T,x,right(i))

    czy_wiekszy(T, x, 0)
    print(ile)


A = [2,5,4,1,7,6]
buildheap(A,len(A))
print(A)
hyhy(A,1)


