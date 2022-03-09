'''. Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).'''

def partition(T, left, right):
    pivot = T[right]
    border = left - 1
    for i in range(left, right):
        if T[i] < pivot:
            border += 1
            T[i], T[border] = T[border], T[i]
    border += 1
    T[border], T[right] = T[right], T[border]
    return border


def select(A, left, right, k):
    if left == right:
        return A[left]
    q = partition(A, left, right)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, left, q - 1, k)
    else:
        return select(A, q + 1, right, k)

def zadanko(A,start,stop):
    x = select(A,0,len(A)-1,start)
    y = select(A,0,len(A)-1,stop)
    sum = 0
    for i in range(len(A)):
        if A[i] >= x and A[i] <= y:
            sum += A[i]
    return sum

T = [2,5,4,7,6,9,8]
print(zadanko(T,2,4))
T = sorted(T)
print(T)