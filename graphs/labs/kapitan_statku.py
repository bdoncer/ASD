def kapitan(G,T):
    n = len(G)
    m = len(G[0])
    steps = [[1,0],[0,1],[-1,0],[0,-1]]
    def DFS_visit(G, x,y):
        visited[x][y] = True
        for step in steps:
            if 0 <= x+step[0] and x+step[0] < n and 0 <=y+step[1] and y+step[1] <m and G[x+step[0]][y+step[1]] >= T and visited[x+step[0]][y+step[1]] == False:
                DFS_visit(G,x+step[0],y+step[1])

    visited = [[False]*m for _ in range(n)]
    DFS_visit(G, 0,0)
    for line in visited:
        print(line)
    print(visited[n-1][m-1])



A = [[1,4,2],
     [2,3,4],
     [1,2,3],
     [3,3,3]]
kapitan(A,3)


