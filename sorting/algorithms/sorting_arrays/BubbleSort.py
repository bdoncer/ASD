#stabilny
def BubbleSort(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1-i):
            if T[j] > T[j+1]:
                T[j],T[j+1] = T[j+1],T[j]

def BubbleSort_reverse(T):
    n = len(T)
    for i in range(n-1):
        for j in range(n-1-i):
            if T[j] < T[j+1]:
                T[j],T[j+1] = T[j+1],T[j]


t = [3,6,84,8,4,8,55,7]
BubbleSort_reverse(t)
print(t)
