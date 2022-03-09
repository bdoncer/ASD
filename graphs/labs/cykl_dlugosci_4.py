from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [-1]*n
    parent = [None]*n
    visited[s] = 0
    Q.put(s)
    sciezka = []
    while not Q.empty():
        i = Q.get()
        for j in range(len(G[i])):
            if G[i][j] != 0:
                neigh = j
                if visited[neigh] == -1:
                    visited[neigh] = visited[i] + 1
                    parent[neigh] = i
                    if visited[neigh] < 2:
                        Q.put(neigh)
                elif visited[i] == 1 and visited[neigh] == 2:
                    sciezka.append(s)
                    sciezka.append(i)
                    sciezka.append(neigh)
                    sciezka.append(parent[neigh])
                    print(sciezka)
                    return True

def cykl(G):
    for i in range(len(G)):
        if BFS(G,i):
            return True
    return False

G = [[0,1,0,0,0],[1,0,1,0,1],[0,0,0,1,0],[0,1,0,0,0],[1,0,0,1,0]]
print(cykl(G))