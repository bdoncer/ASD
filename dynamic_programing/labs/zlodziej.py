def zlodziej(A):
    n = len(A)
    F = [0]*n
    F[0]=A[0]
    F[1] = max(A[0],A[1])
    for i in range(2,n-1):
        F[i] = max(F[i-1],F[i-2]+A[i])
    if F[n-2] > F[n-3]+A[n-1]:
        print(n-2)
        last = n-2
        F[n-1] = F[n-2]
    else:
        print(n-1)
        last = n-1
        F[n-1] = F[n-3]+A[n-1]
    while last > 1:
        if F[last] == F[last-1]:
            last = last - 1
        else:
            print(last-2)
            last = last - 2
    return F[n-1]











wartosci = [20, 1, 3, 7, 21, 1, 10, 18]
print(zlodziej(wartosci))

#f(i)-max wartosc w i f(i)=max(f(i-1),f(i-2)+w(i))