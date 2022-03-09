def same(a, b, n, i1, i2, min, max):
    j, k = i1, i2
    while j < n:
        if (a[j] > min and a[j] < max):
            break
        j += 1
    while k < n:
        if (b[k] > min and b[k] < max):
            break
        k += 1
    if (j == n and k == n):
        return True
    if (((j == n) ^ (k == n)) or a[j] != b[k]):
        return False

    return same(a, b, n, j + 1, k + 1, a[j], max) and same(a, b, n, j + 1, k + 1, min,
                                                                             a[j])  # Left Subtree

def main(a, b, n):
    return same(a, b, n, 0, 0, -10 ** 9, 10 ** 9)