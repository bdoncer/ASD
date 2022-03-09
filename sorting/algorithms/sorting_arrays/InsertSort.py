#stabilny
def InsertSort(T):
    for i in range(1,len(T)):
        key = T[i]
        j = i - 1
        while key < T[j] and j >= 0:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key

def InsertSort_reverse(T):
    for i in range(1,len(T)):
        key = T[i]
        j = i - 1
        while key > T[j] and j >= 0:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key

t = [3,6,84,8,4,8,55,7]
InsertSort_reverse(t)
print(t)

