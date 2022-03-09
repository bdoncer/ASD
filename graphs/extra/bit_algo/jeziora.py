def ile_jezior(G):
    n = len(G)
    steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def DFS_visit(G, x, y):
        nonlocal wielkosc
        visited[x][y] = True
        for step in steps:
            if 0 <= x + step[0] and x + step[0] < n and 0 <= y + step[1] and y + step[1] < n and G[x+step[0]][y+step[1]] == -1 and visited[x + step[0]][y + step[1]] == False:
                DFS_visit(G, x + step[0], y + step[1])
                wielkosc += 1


    visited = [[False] * n for _ in range(n)]
    ile = 0
    for x in range(len(G)):
        for y in range(len(G)):
            if visited[x][y] == False and G[x][y] == 0:
                ile += 1
                wielkosc = 1
                DFS_visit(G,x,y)
                print(wielkosc)
    return ile
#najkrotsza sciezka miedzy lewym gornym a prawym dolnym
from queue import Queue
def sciezka(G):
    Q = Queue()
    steps = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[False] * len(G) for _ in range(len(G))]
    parent = [[None] * len(G) for _ in range(len(G))]
    visited[0][0] = True
    Q.put((0,0))
    while not Q.empty():
        x,y = Q.get()
        for step in steps:
            if 0 <= x + step[0] and x + step[0] < len(G) and 0 <= y + step[1] and y + step[1] < len(G) and G[x+step[0]][y+step[1]] == -1 and visited[x + step[0]][y + step[1]] == False:
                visited[x+step[0]][y+step[1]] = True
                parent[x+step[0]][y+step[1]] = [x,y]
                Q.put((x+step[0],y+step[1]))
    for line in parent:
        print(line)
    while parent[x][y] != None:
        print(x, y)
        x,y = parent[x][y]

    print(x, y)



map = [
    [-1, -1],
    [-1, -1]]


print(sciezka(map))

