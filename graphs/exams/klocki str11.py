#f(i) najwyzsza wieza konczaca sie na itym klocku

def klocki(T):
    n = len(T)
    F = [1]*n
    for i in range(1,n):
        for k in range(i):
            if T[i][0] >= T[k][0] and T[i][1] <= T[k][1]:
                F[i] = max(F[i],F[k]+1)
    res = 0
    print(F)
    for i in range(n):
        if F[i] > res:
            res = F[i]
    return res




A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
B = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(klocki(B))