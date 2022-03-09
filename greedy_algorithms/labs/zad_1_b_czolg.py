from math import inf
def cheapest_path(s, p, l, target):
    n = len(s)
    pos = s[0]
    i = 0
    cost = 0
    fuel = l
    # Dojedź od startu do pierwszej stacji
    fuel -= s[0]
    while pos != target:
        # Jeżeli starczy już paliwa  aby dojechać, to dojedź
        if pos + fuel >= target:
            break
        cheapest = i
        for j in range(i+1, n):
            if p[j] < p[cheapest] and s[j]-pos <= l:
                cheapest = j
                break
        if s[cheapest] == pos:
            # Dotankuj do pełna lub tyle aby dojechać do celu
            cost += min((target-pos-fuel)*p[i], (l-fuel) * p[i])
            fuel = l
            # Przejedź na następną stację i rozważ opcje
            fuel -= s[i+1] - pos
            i += 1
            pos = s[i]
        elif fuel < s[cheapest]-pos:
            cost += min((target-pos-fuel)*p[i], (s[cheapest]-pos-fuel) * p[i])
            # Dotankuj odpowiednią ilość
            fuel += s[cheapest]-pos-fuel
            # Dojedź do celu
            fuel -= s[cheapest] - s[i]
            i = cheapest
            pos = s[i]
        else:
            fuel -= s[cheapest] - pos
            i = cheapest
            pos = s[i]
    return cost
