def merge(A, aux, low, mid, high, count):
    k = i = low
    j = mid + 1
    c = 0

    # run if there are elements in the left and right runs
    while i <= mid and j <= high:

        if A[i] > A[j]:
            # update surpasser count of `A[i]`
            count[A[i]] += c
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            c = c + 1

        k = k + 1

    # copy remaining elements
    while i <= mid:
        count[i] += c
        aux[k] = A[i]
        k = k + 1
        i = i + 1

    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''

    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]



def mergesort(A, aux, low, high, count):

    if high <= low:
        return

    # find midpoint
    mid = low + ((high - low) >> 1)

    # recursively split runs into two halves until run size == 1,
    # merge them, and return up the call chain

    mergesort(A, aux, low, mid, count)
    mergesort(A, aux, mid + 1, high, count)

    merge(A, aux, low, mid, high, count)


def main(A):


    # create two copies of the original list
    aux = A.copy()
    A = A.copy()
    count = [0]*len(A)
    # sort the list in descending order using auxiliary space `aux`
    mergesort(A, aux, 0, len(A) - 1,count)

    return count
T = [3,4,2,5,3,5]
print(main(T))