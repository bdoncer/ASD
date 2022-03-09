'''Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba
 z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową'''

def partition(T,left,right):
    pivot = T[right]
    border = left - 1
    for i in range(left,right+1):
        if T[i] < pivot:
            border += 1
            if border != i:
                T[i],T[border] = T[border],T[i]

    if border + 1 != right:
        T[border+1],T[right] = T[right],T[border+1]
    return border

def quicksort(T,left,right):
    while left < right:
        border = partition(T,left,right)
        if border - left + 1 < right - border - 1:
            quicksort(T,left,border)
            left = border + 2
        else:
            quicksort(T, border + 2, right)
            right = border

def sum(T):
    quicksort(T,0,len(T)-1)
    ctr = 0
    for i in range(len(T)):
        start = 0
        end = len(T)-1
        while start < end:
            if start == i:
                start += 1
                continue
            if end == i:
                end -= 1
                continue
            suma = T[start] + T[end]
            if suma == T[i]:
                ctr += 1
                break
            if suma < T[i]:
                start += 1
            else:
                end -= 1

    if ctr == len(T):
        return True
    else:
        return False

T = [-6,-3,-3,-2,-1,-1,1,1,2,5]
print(sum(T))