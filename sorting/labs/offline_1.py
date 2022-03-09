from random import randint, seed

def merge(T, left, middle, right):
    T_left = [0 for _ in range(middle - left + 1)]
    T_right = [0 for _ in range(right - middle)]
    curr = left
    for i in range(len(T_left)):
        T_left[i] = T[curr]
        curr += 1
    for i in range(len(T_right)):
        T_right[i] = T[curr]
        curr += 1
    finger1 = 0
    finger2 = 0
    curr = left
    while finger1 < len(T_left) and finger2 < len(T_right):
        if T_left[finger1] <= T_right[finger2]:
            T[curr] = T_left[finger1]
            finger1 += 1
        else:
            T[curr] = T_right[finger2]
            finger2 += 1
        curr += 1
    while finger1 < len(T_left):
        T[curr] = T_left[finger1]
        finger1 += 1
        curr += 1


def sort(T, left, right):
    if left >= right:
        return
    middle = (left + right) // 2
    sort(T, left, middle)
    sort(T, middle + 1, right)
    merge(T, left, middle, right)


def mergesort(T):
    sort(T, 0, len(T) - 1)
    return T


seed(42)

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)

T = mergesort(T)

print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK")

