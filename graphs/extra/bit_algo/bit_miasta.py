def obetnij_to_gowno(G,miasta):
    def DFS_visit(G, i):
        res = miasta[i]
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False:
                res = DFS_visit(G, neigh) or res
        if res == False:
            zniszczenie[i] = True
        return res
    n = len(G)
    visited = [False] * n
    zniszczenie = [False] * n
    DFS_visit(G, 0)
    return zniszczenie

from queue import Queue
def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    d = [-1]*n
    parent = [None]*n
    visited[s] = True
    d[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for neigh in G[u]:
            if visited[neigh] == False:
                visited[neigh] = True
                d[neigh] = d[u] + 1
                parent[neigh] = u
                Q.put(neigh)
    return d,parent
def znajdz_sciezke(G):
    odleglosci,rodzice= BFS(G,0)
    max_odl = [0,-1]
    for i in range(len(odleglosci)):
        if odleglosci[i] > max_odl[0]:
            max_odl = [odleglosci[i],i]
    odleglosci,rodzice = BFS(G,max_odl[1])
    max_odl2 = [0, -1]
    for i in range(len(odleglosci)):
        if odleglosci[i] > max_odl2[0]:
            max_odl2 = [odleglosci[i],i]
    #poczatek w max_odl[0],koniec w max_odl[1]
    sciezka_ma_lalala = [False]*len(G)
    index = max_odl2[1]
    while index != max_odl[1]:
        sciezka_ma_lalala[index] = True
        index = rodzice[index]
    sciezka_ma_lalala[max_odl[1]] = True
    return sciezka_ma_lalala

def asdpierdolsie(G,miasta):
    def DFS_visit(G, i):
        nonlocal res
        res += 2
        visited[i] = True
        for neigh in G[i]:
            if visited[neigh] == False and zniszczenie[neigh] == False:
                DFS_visit(G, neigh)

    zniszczenie = obetnij_to_gowno(G,miasta)
    sciezka = znajdz_sciezke(G)
    res = 0
    visited = [False]*len(G)
    for i in range(len(sciezka)):
        if sciezka[i] == True:
            if len(G[i]) > 2:
                for neigh in G[i]:
                    if sciezka[neigh] == False:
                        visited[i] = True
                        DFS_visit(G,neigh)
            res += 1
    return res-1






G = [
    [1],
    [0, 2],
    [1,3],
    [2,4],
    [3,10,5],
    [4,6],
    [5,7],
    [6,8],
    [7,9],
    [8],
    [4,11,12],
    [10, 13,14],
    [10,15,16],
    [11],
    [11],
    [12],
    [12]
]
cities = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
print(asdpierdolsie(G,cities))
