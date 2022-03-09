def binary_search(T, x, left, right):
    while left <= right:
        middle = left + (right - left) // 2
        if T[middle] == x:
            return middle
        if T[middle] != None and T[middle] < x:
            left = middle + 1
        if T[middle]==None or T[middle] > x:
            right = middle - 1
    return False

T = [1,4,6,12,34,567,None,None,None]
print(binary_search(T,567,0,len(T)-1))
