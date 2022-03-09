def jezioro(T):
    n = len(T)
    ctr = 1
    res = 0
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                old_res = res
                res = 0
                res = DFS(T, i, j, n, ctr)
                res = max(res, old_res)
                ctr += 1
    for line in T:
        print(line)
    return res


def DFS(T, i, j, n, ctr):
    T[i][j] = ctr
    res = 1
    if i > 0 and T[i - 1][j] == 0:
        res += DFS(T, i - 1, j, n, ctr)
    if j > 0 and T[i][j - 1] == 0:
        res += DFS(T, i, j - 1, n, ctr)
    if i < n - 1 and T[i + 1][j] == 0:
        res += DFS(T, i + 1, j, n, ctr)
    if j < n - 1 and T[i][j + 1] == 0:
        res += DFS(T, i, j + 1, n, ctr)
    return res


from queue import Queue
def BFS(T, i, j):
    Q = Queue()
    n = len(T)
    Q.put([i, j])
    T[0][0] = 0
    while not Q.empty():
        (i, j) = Q.get()
        d = T[i][j]
        if i > 0 and T[i - 1][j] == -1:
            T[i - 1][j] = d +1
            Q.put((i - 1, j))
        if j > 0 and T[i][j - 1] == -1:
            T[i][j - 1] = d+1
            Q.put((i, j - 1))
        if i < n - 1 and T[i + 1][j] == -1:
            T[i + 1][j] = d+1
            Q.put((i + 1, j))
        if j < n - 1 and T[i][j + 1] == -1:
            T[i][j+1] = d+1
            Q.put((i, j + 1))
    res = T[n-1][n-1]-1
    droga = [(n-1,n-1)]
    i = n -1
    j = n -1
    while res >= 0 :
        if i > 0 and T[i - 1][j] == res:
            droga.append((i-1,j))
            i = i -1
        elif j > 0 and T[i][j - 1] == res:
            droga.append((i, j-1))
            j = j - 1
        elif i < n - 1 and T[i + 1][j] == res:
            droga.append((i + 1, j))
            i = i + 1
        elif j < n - 1 and T[i][j + 1] == res:
            droga.append((i, j+1))
            j = j + 1
        res -= 1
    print(droga)





map = [
    [-1, 0, -1, -1, -1, -1, -1, -1],
    [-1, 0, -1, 0, 0, -1, -1, -1],
    [-1, -1, -1, 0, 0, -1, 0, -1],
    [-1, 0, 0, 0, 0, -1, 0, -1],
    [-1, -1, 0, 0, -1, -1, -1, -1],
    [-1, 0, -1, -1, -1, -1, 0, 0],
    [0, 0, -1, 0, 0, -1, 0, -1],
    [-1, -1, -1, 0, -1, -1, -1, -1],
]
print(BFS(map,0,0))
