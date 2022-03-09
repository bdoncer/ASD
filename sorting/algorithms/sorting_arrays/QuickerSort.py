#partition - n,niestabilny
def partition(T, left,right):
    lo = left
    hi = right
    mid = left
    pivot = T[right]
    while mid <= hi:
        if T[mid] < pivot:
            T[lo], T[mid] = T[mid], T[lo]
            lo = lo + 1
            mid = mid + 1
        elif T[mid] == pivot:
            mid = mid + 1
        else:
            T[mid], T[hi] = T[hi], T[mid]
            hi = hi - 1
    return lo,hi

def QuickSort(T,l,r):
    if l < r:
        start,end = partition(T,l,r)
        QuickSort(T,l,start-1)
        QuickSort(T,end+1,r)

T = [1,3,2,3,1,3,1,1,2,2,5,3,5,2,5,2,4,2,1,4]

QuickSort(T,0,len(T)-1)
print(T)
