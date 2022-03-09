def reverse(G):
    F = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for neigh in G[i]:
            F[neigh].append(i)
    print(F)


G = [[2,3,5],[3,2],[4,3],[3,2],[3,2,5],[]]
reverse(G)