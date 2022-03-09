from math import inf
def shortestDist(graph):
    N = len(graph)+1
    dist = [inf] * N
    dist[N - 1] = 0
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if graph[i][j] == 0:
                continue
            dist[i] = min(dist[i],graph[i][j] + dist[j])
    return dist[0]
a = 0
graph = [[0, 1, 2, 5, 0, 0, 0, a],
         [a, a, a, a, 4, 11, a, a],
         [a, a, a, a, 9, 5, 16, a],
         [a, a, a, a, a, a, 2, a],
         [a, a, a, a, a, a, a, 18],
         [a, a, a, a, a, a, a, 13],
         [a, a, a, a, a, a, a, 2]]
print(shortestDist(graph))