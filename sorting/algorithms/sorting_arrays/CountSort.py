#n+k stabilny
def CountSort(T,k):
    counter = [0] * k
    res = [0] * len(T)
    for i in range(len(T)):
        counter[T[i]] += 1
    for i in range(1, k):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[T[i]] -= 1
        res[counter[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]

