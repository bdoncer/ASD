
def prefix(A):
    n = len(A)
    m = len(A[0])
    sum = [[0]*m for _ in range(n)]
    sum[0][0] = A[0][0]
    for i in range(1,n):

        sum[i][0] = sum[i-1][0] + A[i][0]
    for i in range(1,m):
        sum[0][i] = sum[0][i-1]+A[0][i]

    for i in range(1,n):
        for j in range(1,m):
            sum[i][j] = sum[i][j-1] + sum[i - 1][j] + A[i][j] - sum[i - 1][j -1]
    for line in sum:
        print(line)


A = [[1,2,2],
     [3,4,-10]]
prefix(A)
