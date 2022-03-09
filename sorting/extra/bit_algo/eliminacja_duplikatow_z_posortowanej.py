def eliminuj(A):
    T = [A[0]]
    j = 0
    for i in range(len(A)):
        if A[i] != T[j]:
            T.append(A[i])
            j += 1
    print(T)

A = [1,1,1,2,2,3,4,4,5,6,6,7,9,12,33]
eliminuj(A)