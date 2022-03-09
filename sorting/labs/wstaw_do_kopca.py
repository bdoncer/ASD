def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2


def wstaw_do_kopca(A,val):
    A.append(val)
    i = len(A)-1
    while A[parent(i)] < val and i != 0:
        A[i],A[parent(i)] = A[parent(i)],A[i]
        i = parent(i)
    print(A)


A = [10,7,8,5,6]
wstaw_do_kopca(A,11)
