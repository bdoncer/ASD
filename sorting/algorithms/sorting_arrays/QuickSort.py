#partition - n,niestabilny
def partition(T,l,r):
    pivot = T[r]
    i = l-1
    for j in range(l,r):
        if T[j] <= pivot:
            i+=1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def QuickSort(T,l,r):
    if l < r:
        pivot_ind = partition(T,l,r)
        QuickSort(T,l,pivot_ind-1)
        QuickSort(T,pivot_ind+1,r)

T = [4,63,6,34,6,35,63,4]
QuickSort(T,0,len(T)-1)
print(T)
