def CountSort(T):
    counter = [0] * 27
    res = [0] * len(T)
    for i in range(len(T)):
        counter[ord(T[i])-96] += 1
    for i in range(1, 27):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[ord(T[i])-96] -= 1
        res[counter[ord(T[i])-96]] = T[i]
    return res

#print(CountSort('cndusvb'))



