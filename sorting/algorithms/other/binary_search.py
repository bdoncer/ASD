#logn
def binary_search(T, x, left, right):
    while left <= right:
        middle = left + (right - left) // 2
        if T[middle] == x:
            return middle
        if T[middle] < x:
            left = middle + 1
        if T[middle] > x:
            right = middle - 1
    return False
def binary_search_smallest(T,x,left,right):
    while left <= right:
        middle = left + (right - left) // 2
        if T[middle] == x:
            if middle == 0 or T[middle - 1] != x:
                return middle
            else:
                right = middle-1
        if T[middle] < x:
            left = middle + 1
        if T[middle] > x:
            right = middle - 1
    return False


T = [1,2,3,3]
print(binary_search_smallest(T,3,0,len(T)-1))

