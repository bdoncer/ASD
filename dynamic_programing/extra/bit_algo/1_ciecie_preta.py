def slice(prices, n):
    # Podział na 2 kawałki to 3 [0,1,2]
    n = n + 1
    F = [-1] * n
    F[0] = prices[0]
    F[1] = prices[1]
    for dlugosc in range(2, n):
        F[dlugosc] = prices[dlugosc]
        for odcinany in range(1, dlugosc):
            do_pociecia = dlugosc-odcinany
            if F[dlugosc] < F[do_pociecia] + prices[odcinany]:
                F[dlugosc] = F[do_pociecia] + prices[odcinany]
    print(F)


prices = [0, 5, 8, 9, 10]
slice(prices, 2)