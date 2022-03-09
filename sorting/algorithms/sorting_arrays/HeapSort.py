#nlogn (heapify logn buildheap logn) niestabilny
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


def heapsort(A):
    n = len(A)
    buildheap(A, n)
    for i in range(n - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
