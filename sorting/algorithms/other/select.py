#n
def partition(T, l, r):
    pivot = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] <= pivot:
            i = i + 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1

def select(T, l, r, k):
    if l==r:
        return T[l]
    q = partition(T, l, r)
    if q == k:
        return T[q]
    elif k < q:
        return select(T, l, q - 1, k)
    else:
        return select(T, q + 1, r, k)
