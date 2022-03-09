def SelectSort(T):
    n = len(T)
    for i in range(len(T)):
        index = i
        for j in range(i+1,len(T)):
            if T[index] > T[j]:
                index = j
        T[index],T[i] = T[i],T[index]