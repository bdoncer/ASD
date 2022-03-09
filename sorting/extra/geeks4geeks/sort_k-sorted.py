#nlogn (heapify logn buildheap logn) niestabilny
def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def heapify(A, n, i):
    index = i
    if left(i) < n and A[left(i)] < A[i]:
        index = left(i)
    if right(i) < n and A[right(i)] < A[index]:
        index = right(i)
    if i != index:
        A[i], A[index] = A[index], A[i]
        heapify(A, n, index)

def buildheap(A, n):
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def sort_k(A,k):
    k = k+1
    n = len(A)
    heap = []
    for i in range(k):
        heap.append(A[i])
    buildheap(heap,k)
    res = []
    ind = k
    while ind < n:
        res.append(heap[0])
        del heap[0]
        heap.append(A[ind])
        heapify(heap,len(heap),0)
        ind += 1
    while len(heap) != 0:
        res.append(heap[0])
        del heap[0]
        heapify(heap,len(heap),0)


    return res

A = [10, 9, 8, 7, 4, 70, 60, 50]
print(sort_k(A,4))
