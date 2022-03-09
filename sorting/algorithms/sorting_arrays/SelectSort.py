#niestabilny
def SelectSort(T):
    n = len(T)
    for i in range(len(T)):
        index = i
        for j in range(i+1,len(T)):
            if T[index] > T[j]:
                index = j
        T[index],T[i] = T[i],T[index]

def SelectSort_reverse(T):
    n = len(T)
    for i in range(len(T)):
        index = i
        for j in range(i+1,len(T)):
            if T[index] < T[j]:
                index = j
        T[index],T[i] = T[i],T[index]

t = [1,6,3,8,4,7]
SelectSort_reverse(t)
print(t)