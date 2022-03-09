from queue import Queue
def skoczek(a,b,c,d):
    # od a,b do c,d
    skoki = [(2, -1),( 2,  1),(-2,1),( -2,-1),( 1, 2),( 1, -2),( -1, 2),(-1,  -2)]
    Q = Queue()
    visited = [[False,False] * 8 for _ in range(8)]
    dist = [[-1,-1] * 8 for _ in range(8)]
    visited[a][b] = True
    dist[a][b] = 0
    Q.put((a,b))
    while not Q.empty():
        x,y = Q.get()
        for skok in skoki:
            if 0 <= x + skok[0] < 8 and 0<= y+skok[1]<8:
                if visited[x + skok[0]][y + skok[1]] == False:
                    visited[x + skok[0]][y + skok[1]] = True
                    dist[x + skok[0]][y + skok[1]] = dist[x][y] + 1
                    Q.put((x + skok[0],y + skok[1]))
    return dist[c][d]

print(skoczek(7,0,0,7))