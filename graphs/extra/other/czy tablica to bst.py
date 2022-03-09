from math import inf
def czy_BST(T):
    n = len(T)
    maxx = inf
    minn = -inf
    for i in range(1, n):
        if (T[i] > T[i - 1] and T[i] > minn and T[i] < maxx):
            minn = T[i - 1]
        elif (T[i] < T[i - 1] and T[i] > minn and T[i] < maxx):
            maxx = T[i - 1]
        else:
            return False
    return True

T = [500, 200, 90, 250, 100]
T2 = [5123, 3300, 783, 1111, 890]
print(czy_BST(T2))