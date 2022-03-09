'''2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
pretty_sort(T)
która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''


def found_digit(a, digit):  # digit - ktora cyfra od tylu
    a = a // 10 ** (digit - 1)
    return a % 10


def CountSort(T, pointer):
    counter = [0] * 10
    res = [0] * len(T)
    for i in range(len(T)):
        counter[found_digit(T[i][1], pointer)] += 1
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    for i in range(len(T) - 1, -1, -1):
        counter[found_digit(T[i][1], pointer)] -= 1
        res[counter[found_digit(T[i][1], pointer)]] = T[i]
    for i in range(len(T)):
        T[i] = res[i]


def RadixSort(T):
    n = len(T)
    max_T = T[0][1]
    for i in range(n):
        if T[i][1] > max_T:
            max_T = T[i][1]
    ln = 0
    while max_T > 0:
        ln += 1
        max_T //= 10
    for i in range(1, ln + 1):
        CountSort(T, i)


def liczenie(a):
    cyfry = [0] * 10
    while a != 0:
        cyfry[a % 10] += 1
        a = a // 10
    ile_jednokrotnych = 0
    ile_wielokrotnych = 0
    for i in range(len(cyfry)):
        if cyfry[i] == 1:
            ile_jednokrotnych += 1
        if cyfry[i] > 1:
            ile_wielokrotnych += 1
    odp = 10 * ile_jednokrotnych + (9-ile_wielokrotnych)
    return odp


def pretty_sort(T):
    for i in range(len(T)):
        odp = liczenie(T[i])
        T[i] = (T[i], odp)
    RadixSort(T)
    for i in range(len(T)):
        T[i] = T[i][0]


T = [123,455,55555,554433454545359086406]
pretty_sort(T)
print(T)
