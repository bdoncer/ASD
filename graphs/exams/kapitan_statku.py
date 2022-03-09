from queue import Queue
def kapitan(G,t):
    Q = Queue()
    n = len(G)  # ilosc wierzcholkow
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    Q.put((0,0))
    while not Q.empty():
        i,j = Q.get()
        if i > 0 and visited[i-1][j] == False and G[i-1][j] > t:
            visited[i-1][j] = True
            Q.put((i-1,j))
        if j > 0 and visited[i][j-1] == False and G[i][j-1] > t:
            visited[i][j-1] = True
            Q.put((i,j-1))
        if i < n-1 and visited[i+1][j] == False and G[i+1][j] > t:
            visited[i+1][j] = True
            Q.put((i+1,j))
        if j < n-1 and visited[i][j+1] == False and G[i][j+1] > t:
            visited[i][j+1] = True
            Q.put((i, j+1))
    print(visited)



G = [[3,4,6],
     [1,1,4],
     [3,3,3]]
kapitan(G,2)