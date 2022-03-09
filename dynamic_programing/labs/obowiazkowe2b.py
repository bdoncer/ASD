from math import inf
def min_koszt(miejsca,ceny,bak):
    n = len(miejsca)
    F = [inf]*(n)
    F[0] = miejsca[0]*ceny[0]
    for i in range(1,n):
        for k in range(i):
            if miejsca[i]-miejsca[k] <= bak:
                F[i] = min(F[i],F[k]+ceny[i]*(miejsca[i]-miejsca[k]))
    res = inf
    i = n-2
    while miejsca[n-1]-miejsca[i] <= bak:
        res = min(res,F[i])
        i -= 1
    return res

p = [1, 2, 3, 4, 5, 6, 7]
s = [3, 6, 7, 9, 12, 13, 15]
print(min_koszt(s,p,5))