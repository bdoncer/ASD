def najdluzszy_rosnacy(T):
    n = len(T)
    A = [1] * n
    ktory_przedluza = [[] for _ in range(n)]
    max_dlugosc = 1
    #szukam malejących w tablicy od tylu (czyli od przodu beda one rosnace)
    for i in range(n-1,-1,-1):
        for j in range(i + 1, n):
            if T[j] > T[i] and A[j] + 1 == A[i]:
                ktory_przedluza[i].append(j)
            if T[j] > T[i] and A[j] + 1 > A[i]:
                A[i] = A[j] + 1
                ktory_przedluza[i] = [j]
        max_dlugosc = max(A[i],max_dlugosc)
    ile = 0
    print(ktory_przedluza)
    for i in range(n):
        if A[i] == max_dlugosc:
            ile += wypisz_wynik(T,ktory_przedluza,i)
    return ile

def wypisz_wynik(T,ktory_przedluza,index,res = []):
    if len(ktory_przedluza[index]) == 0:
        for i in range(len(res)):
            print(res[i],end = ' ')
        print("")
        return 1
    ile = 0
    for i in range(len(ktory_przedluza[index])):
        if len(res) == 0:
            res += [T[index]]
        res += [T[ktory_przedluza[index][i]]]
        ile += wypisz_wynik(T,ktory_przedluza,ktory_przedluza[index][i],res)
    return ile



arr = [2,1,4,3]
print(najdluzszy_rosnacy(arr))
