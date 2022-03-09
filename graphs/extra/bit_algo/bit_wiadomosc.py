from queue import Queue
def BFS(T,s,n):
    G = [[] for _ in range(n)]
    for i in range(len(T)):
        G[T[i][0]].append(T[i][1])
        G[T[i][0]].append(T[i][1])
    Q = Queue()
    visited = [False]*n
    d = [-1]*n
    visited[s] = True
    d[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            if visited[neigh] == False:
                visited[neigh] = True
                d[neigh] = d[u] + 1
                Q.put(neigh)
    maxx = 0
    for i in range(n):
       maxx = max(maxx,d[i])
    res_max = [0,-1]
    for i in range(1,maxx):
        res = 0
        for j in range(n):
            if d[j] == i:
                res += 1
        if res > res_max[0]:
            res_max = [res,i]
    return res_max[1],res_max[0]



meh1 = [[0, 1], [1, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 7], [4, 7], [4, 8], [5, 8], [5, 9], [6, 9], [7, 10], [8, 10],
       [9, 10]]
print(BFS(meh1,0,11))




