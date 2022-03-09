def CountSort(T, pointer):
    counter = [0] * 27
    res = [0] * len(T)
    for i in range(len(T)):
        if pointer < len(T[i]):
            counter[ord(T[i][pointer])-96] += 1
        else:
            counter[0] += 1
    for i in range(1, 27):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        if pointer < len(T[i]):
            counter[ord(T[i][pointer])-96] -= 1
            res[counter[ord(T[i][pointer])-96]] = T[i]
        else:
            counter[0] -= 1
            res[counter[0]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]

def RadixSort(T):
    n = len(T)
    max_T = len(T[0])
    for i in range(n):
        if len(T[i]) > max_T:
            max_T = len(T[i])
    for i in range(max_T-1,-1,-1):
        CountSort(T, i)


T = ['other', 'cbdgfg', 'abdwnfu', 'andndue', 'dffejivuwg','dffejixuwg']
RadixSort(T)
print(T)
