def binary_search(T, x, left, right):
    while left <= right:
        middle = left + (right - left) // 2
        if T[middle] == x:
            if abs(T[middle-1] - x) < abs(T[middle + 1] - x):
                return middle -1
            else:
                return middle + 1
        if T[middle] < x:
            if middle +1 >= len(T):
                return middle
            if T[middle+1] > x:
                if abs(T[middle]-x) < abs(T[middle+1]-x):
                    return middle
                else:
                    return middle+1
            left = middle + 1
        if T[middle] > x:
            if middle-1<0:
                return middle
            if T[middle-1] < x:
                if abs(T[middle]-x) < abs(T[middle]-x):
                    return middle
                else:
                    return middle-1
            right = middle - 1

def znajdz(A,x,k):
    res = []
    index = binary_search(A,x,0,len(A)-1)
    res.append(A[index])
    left = index-1
    right=index+1
    while len(res) != k:
        if left >= 0 and A[left] == x:
            left -=1
        if right < len(A) and A[right] == x:
            right+=1
        if left < 0:
            res.append(A[right])

            right += 1
            continue
        if right >= len(A):
            res.append(A[left])
            left -= 1
            continue

        if left >= 0 and right < len(A) and abs(A[left] - x) < abs(A[right] - x):
            res.append(A[left])
            left -= 1
        else:
            if right < len(A):
                res.append(A[right])
                right += 1

    print(res)

t = [12, 16, 22, 30, 35, 39, 42,
               45, 48, 50, 53, 55, 56]
k = 4
x = 49
znajdz(t,x,k)
