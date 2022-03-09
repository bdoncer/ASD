def czy_sumowanie(A,x):
    F = [[False]*(x+1) for _ in range(len(A))]
    for i in range(len(A)):
        F[i][0] = True
    F[0][A[0]] = True
    for i in range(1,len(A)):
        for j in range(x+1):
            F[i][j] = F[i-1][j]
            if j-A[i] >= 0:
                F[i][j] = F[i][j] or F[i-1][j-A[i]]
    i = len(A)-1
    j = x
    sum = 0
    while sum != x:
        while i>=1 and  F[i-1][j] == True:
            i -= 1
        print(i)
        j = j-A[i]
        sum += A[i]
        i -= 1


    #return get_solution(A,F,len(A)-1,x)


def get_solution(A,F,w,k):
    if w == 0:
        if k != 0 and F[0][k] == True:
            return [0]
        else:
            return []
    if F[w-1][k] == True:
        return get_solution(A,F,w-1,k)
    else:
        return get_solution(A,F,w-1,k-A[w])+[w]

