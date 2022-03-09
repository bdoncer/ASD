def ugly(n):
    nbr = [1]*(n)
    tres = 0
    dos = 0
    funf = 0
    for i in range(1,n):
        nbr[i] = min(nbr[tres]*3,nbr[dos]*2,nbr[funf]*5)
        if nbr[i] == nbr[tres]*3:
            tres+=1
        elif nbr[i] == nbr[dos]*2:
            dos+=1
        elif nbr[i] == nbr[funf]*5:
            funf+=1
    print(nbr)
    return nbr[n-1]



print(ugly(7))