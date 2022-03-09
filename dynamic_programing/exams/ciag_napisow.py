def czy_git(A,k,t,i,j):
    if len(A[k]) == j-i+1:
        ind = 0
        for p in range(i,j+1):
            if A[k][ind] != t[p]:
                return False
            ind+=1
    else:
        return False
    return True
def napisy(A,t):
    n = len(t)
    F = [[0]*n for _ in range(n)]
    for k in range(len(A)): #ktore slowo
        for i in range(n): #odkad
            for j in range(i,n): #dokad
                if czy_git(A,k,t,i,j) == True:
                    F[i][j] = j-i+1
    return rec(F,t,0,n-1)
def rec(F,t,i,j):
    if F[i][j] != 0:
        return F[i][j]
    for k in range(i,j):
        F[i][j] = max(F[i][j],min(rec(F,t,i,k),rec(F,t,k+1,j)))
    return F[i][j]

S=["ab", "abab", "ba", "bab", "b"]
t = "ababbab"
print(napisy(S,t))






