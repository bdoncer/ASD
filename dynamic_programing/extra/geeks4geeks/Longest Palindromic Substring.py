def czy_palindrom(s,x,y,F):
    n = len(s)
    return rec(s,F,x,y)
def rec(s,F,x,y):
    if F[x][y] != None:
        return F[x][y]
    if x==y:
        F[x][y] = True
        return True
    if x+1 == y or x-1==y:
        if s[x]==s[y]:
            F[x][y] = True
            return F[x][y]
    n = len(s)
    if s[x] == s[y]:
        F[x][y] = rec(s,F,x+1,y-1)
    if F[x][y] == None:
        F[x][y] = False
    return F[x][y]

def longest(A):
    n=len(A)
    res = 0
    F = [[None]*n for _ in range(n)]
    start = -1
    for i in range(len(A)):
        for j in range(i,len(A)):
            if czy_palindrom(A,i,j,F) == True:
                if j-i+1>res:
                    res = j-i+1
                    start = i
    for k in range(res):
        print(A[start+k],end="")


longest('forgeeksskeegfor')