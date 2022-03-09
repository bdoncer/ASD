from math import inf
def is_a_word(i,j,S,T):
    word = T[i:j+1]
    for i in range(len(S)):
        if S[i] == word:
            return True
    return False
def stringi(S,T):
    n = len(T)
    F = [[inf]*n for _ in range(n)]
    majtasy(0,n-1,T,F)
    print(F)
    return F[0][n-1]
def majtasy(i,j,T,F):
    if F[i][j] != inf:
        return F[i][j]
    if is_a_word(i,j,S,T):
        F[i][j] = 1
        return F[i][j]
    res = F[i][j]
    for k in range(i,j):
        res = min(res,majtasy(i,k,T,F)+majtasy(k+1,j,T,F))
    F[i][j] = res
    return F[i][j]

S = ["ab","abab","ba","bab","b"]
T = "ababbab"
print(stringi(S,T))