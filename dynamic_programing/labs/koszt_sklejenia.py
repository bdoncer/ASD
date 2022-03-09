from math import inf
def koszt_sklejenia(A,maxx):
    n = len(A)
    F = [[inf]*(maxx+1) for _ in range(maxx+1)]
    F[0][0] = 0
    for i in range(n):
        F[A[i][0]][A[i][1]] = A[i][2]
    x = rec(A,F,0,maxx)
    print(x)

def rec(A,F,i,j):
    if F[i][j] != inf:
        return F[i][j]
    for k in range(i+1,j):
        F[i][j] = min(F[i][j],rec(A,F,i,k)+rec(A,F,k,j))
    return F[i][j]

A = [[0,1,2],[1,2,3],[2,3,3],[2,3,1],[3,4,10],[3,4,1],[0,3,1]]
print(koszt_sklejenia(A,5))