def sciezka(i, j, prev_w, prev_k, T, F, n, m):
    if F[i][j] != -1:
        return F[i][j]
    F[i][j] = 1
    w = i + 1
    k = j
    if w < n and w != prev_w and T[w][k] > T[i][j]:
        F[i][j] = max(F[i][j],sciezka(w, k, i, j, T, F, n, m)+1)
    w = i
    k = j + 1
    if k < m and k != prev_k and T[w][k] > T[i][j]:
        F[i][j] = max(F[i][j],sciezka(w, k, i, j, T, F, n, m)+1)
    w = i - 1
    k = j
    if w >= 0 and w != prev_w and T[w][k] > T[i][j]:
        F[i][j] = max(F[i][j],sciezka(w, k, i, j, T, F, n, m)+1)
    w = i
    k = j - 1
    if k >= 0 and k != prev_k and T[w][k] > T[i][j]:
        F[i][j] = max(F[i][j],sciezka(w, k, i, j, T, F, n, m)+1)
    return F[i][j]

def main(i, j, T):
    n = len(T)
    m = len(T[0])
    F = [[-1] * m for _ in range(n)]
    sciezka(i,j,-1,-1,T,F,n,m)
    print(F)


T = [[1,2,3],[8,9,4],[7,6,5]]
main(0,0,T)