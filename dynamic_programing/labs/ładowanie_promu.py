def prom(A,L):
    n = len(A)
    F = [[[0]*(L+1) for _ in range(L+1)] for _ in range(n)]
    if A[0] < L+1:
        F[0][A[0]][0] = 1
        F[0][0][A[0]] = 1
    for i in range(1,n):
        for left in range(L+1):
            for right in range(L+1):
                F[i][left][right] = F[i-1][left][right]
                if A[i] == right and left == 0:
                    F[i][left][right] = max(F[i][left][right], 1)
                if A[i] == left and right == 0:
                    F[i][left][right] = max(F[i][left][right], 1)
                if left-A[i]  >= 0 and F[i-1][left-A[i]][right] != 0:
                    F[i][left][right] = max(F[i][left][right],F[i-1][left-A[i]][right]+1)
                if right-A[i]  >= 0 and F[i-1][left][right-A[i]] != 0:
                    F[i][left][right] = max(F[i][left][right],F[i-1][left][right-A[i]]+1)
    res = 0
    l=0
    r=0
    for left in range(L+1):
        for right in range(L+1):
            if F[n-1][left][right] > res:
                res = F[n-1][left][right]
                l = left
                r = right
    print_solution(A,F,n-1,l,r,res,ctr = 0)
    return F[n-1][L][L]

def print_solution(A,F,i,left,right,res,ctr = 0):
    if ctr == res:
        return
    if left-A[i] >= 0 and F[i][left][right] == F[i-1][left-A[i]][right]+1 and F[i-1][left-A[i]][right] != 0:
        print(A[i],'left')
        print_solution(A,F,i-1,left-A[i],right,res,ctr+1)
    elif right-A[i] >= 0 and F[i][left][right] == F[i-1][left][right-A[i]]+1 and F[i-1][left-A[i]][right] != 0:
        print(A[i],'right')
        print_solution(A,F,i-1,left,right-A[i],res,ctr+1)
    elif F[i][left][right] == F[i-1][left][right]:
        print_solution(A, F, i - 1, left, right, res, ctr)
    else:
        if left == 0:
            print(A[i],'right')
            print_solution(A, F, i - 1, left, right - A[i], res, ctr + 1)
        else:
            print(A[i],'left')
            print_solution(A, F, i - 1, left - A[i], right, res, ctr + 1)





A = [1,1,4,3,2,1,1]
print(prom(A,5))