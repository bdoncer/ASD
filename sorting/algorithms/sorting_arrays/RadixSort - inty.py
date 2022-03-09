def found_digit(a, digit):  # digit - ktora cyfra od tylu
    a = a // 10 ** (digit - 1)
    return a % 10


def CountSort(T, pointer):
    counter = [0] * 10
    res = [0] * len(T)
    for i in range(len(T)):
        counter[found_digit(T[i], pointer)] += 1
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[found_digit(T[i], pointer)] -= 1
        res[counter[found_digit(T[i], pointer)]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]


def RadixSort(T):
    n = len(T)
    max_T = T[0]
    for i in range(n):
        if T[i] > max_T:
            max_T = T[i]
    ln = 0
    while max_T > 0:
        ln += 1
        max_T //= 10
    for i in range(1, ln + 1):
        CountSort(T, i)


T = [4, 35, 34, 43, 43, 55, 4, 45]
RadixSort(T)
print(T)


def CountSort_reverse(T, pointer):
    counter = [0] * 10
    res = [0] * len(T)
    for i in range(len(T)):
        counter[9 - found_digit(T[i], pointer)] += 1
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[9 - found_digit(T[i], pointer)] -= 1
        res[counter[9 - found_digit(T[i], pointer)]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]