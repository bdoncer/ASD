'''3.Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based heap).
Mając daną liczbę rzeczywistą x sprawdź, czy k-ty najmniejszy element jest większy lub równy x.'''

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

def funkcja(A,x,i=0):
    ctr = 0
    if A[i] < x:
        ctr += 1
        if left(i) < len(A) and A[left(i)] < x:
            ctr += funkcja(A,x,left(i))
        if right(i) < len(A) and A[right(i)] < x:
            ctr += funkcja(A,x,right(i))
    return ctr
def main(A,k,x):
    ctr = funkcja(A,x)
    print(ctr)
    if ctr+1 <= k:
        return True
    return False


A = [7, 7, 1, 5, 9, 8, 7, 5, 8, 6]
buildheap(A,len(A))
print(A)
print(main(A,4,7))