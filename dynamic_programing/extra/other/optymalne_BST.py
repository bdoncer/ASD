from math import inf
def optymalne(keys, freq, n):
    cost = [[0 for x in range(n)]
            for y in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]
    for L in range(2, n + 1): #dlugosc
        for i in range(n - L + 2): #odkad
            j = i + L - 1 #dokad
            if i >= n or j >= n:
                break
            cost[i][j] = inf
            for root in range(i, j + 1):
                c = 0
                if (root > i):
                    c += cost[i][root - 1]
                if (root < j):
                    c += cost[root + 1][j]
                c += sum(freq, i, j)
                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]


def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s
