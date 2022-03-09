from queue import Queue
def kings_path(G):
    Q = Queue()
    visited = [[False]*len(G) for _ in range(len(G))]
    dist = [[-1] * len(G) for _ in range(len(G))]
    lewo = [[-1] * len(G) for _ in range(len(G))]
    prawo = [[-1] * len(G) for _ in range(len(G))]
    gora = [[-1] * len(G) for _ in range(len(G))]
    dol = [[-1] * len(G) for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            lewo[i][j] = G[i][j]
            prawo[i][j] = G[i][j]
            gora[i][j] = G[i][j]
            dol[i][j] = G[i][j]
    visited[0][0] = 1
    dist[0][0] = G[0][0]
    Q.put((0,0))
    while not Q.empty():
        x,y = Q.get()
        if x-1 > 0 and visited[x-1][y] != True:
            if gora[x-1][y] == 1:
                dist[x-1][y] = dist[x][y] + G[x-1][y]
                visited[x-1][y] == True
                Q.put((x - 1, y))
            else:
                gora[x - 1][y] -= 1
                Q.put((x,y))

        if y-1 > 0 and visited[x][y-1] != True:
            if lewo[x][y-1] == 1:
                visited[x][y-1] == True
                dist[x][y-1] = dist[x][y] + G[x][y-1]
                Q.put((x, y-1))
            else:
                lewo[x][y-1] -= 1
                Q.put((x, y))

        if x+1 < len(G) and visited[x+1][y] != True:
            if dol[x+1][y] == 1:
                visited[x+1][y] = True
                dist[x+1][y] = dist[x][y] + G[x+1][y]
                Q.put((x +1, y))
            else:
                dol[x + 1][y] -= 1
                Q.put((x, y))

        if y + 1 < len(G) and visited[x][y+1] != True:
            if prawo[x][y + 1] == 1:
                visited[x][y + 1] = True
                dist[x][y + 1] = dist[x][y] + G[x][y + 1]
                Q.put((x, y+1))
            else:
                prawo[x][y + 1] -= 1
                Q.put((x, y))

    for line in dist:
        print(line)


A = [[1,4,8],
     [2,3,1],
     [3,2,5]]
kings_path(A)