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
#na ile sposobow mozna pociac wyraz na palindromy
from math import inf
def main(s):
    n = len(s)
    P = [inf]*n
    F = [[None]*n for _ in range(n)]
    P[0] = 1
    for i in range(1,n):
        for j in range(i+1):
            if j!= 0 and P[j-1]+1<P[i]:
                pal = czy_palindrom(s,j,i,F)
                if  pal == True:
                    P[i] = P[j-1]+1
            if j == 0:
                if czy_palindrom(s,0,i,F) == True:
                    P[i] = 1
    print(P)
    return P[n-1]-1

print(main('dwubwcwb'))
