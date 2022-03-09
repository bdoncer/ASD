'''7.Dane są trzy zbiory reprezentowane przez tablice: A, B i C. Napisz algorytm, który powie, czy istnieje
taka trójka a, b, c z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!'''

from random import randint, seed


def partition(T, left, right):
    pivot = T[right]
    border = left - 1
    for i in range(left, right + 1):
        if T[i] < pivot:
            border += 1
            if border != i:
                T[i], T[border] = T[border], T[i]

    if border + 1 != right:
        T[border + 1], T[right] = T[right], T[border + 1]
    return border


def sort(T, left, right):
    while left < right:
        border = partition(T, left, right)
        if border - left + 1 < right - border - 1:
            sort(T, left, border)
            left = border + 2
        else:
            sort(T, border + 2, right)
            right = border


def find(A, B, x):
    finger1 = 0
    finger2 = len(B) - 1
    while finger1 < len(A) and finger2 >= 0:
        if A[finger1] + B[finger2] == x:
            return True
        else:
            if A[finger1] + B[finger2] < x:
                finger1 += 1
            else:
                finger2 -= 1
    if finger1 == len(A):
        finger1 -= 1
        while finger2 >= 0:
            if A[finger1] + B[finger2] == x:
                return True
            finger2 -= 1
    elif finger2 == -1:
        finger2 += 1
        while finger1 < len(A):
            if A[finger1] + B[finger2] == x:
                return True
            finger1 += 1
    return False


def literki(A, B, C):
    sort(A, 0, len(A) - 1) #aloga
    sort(B, 0, len(B) - 1)#blogb
    for i in range(len(C)):#c
        if find(A, B, C[i]):#a+b
            return True
    return False


n = 10
arr_a = [randint(1, 100) for _ in range(5)]
arr_b = [randint(1, 100) for _ in range(5)]
arr_c = [randint(5, 200) for _ in range(1)]
print(arr_a, arr_b, arr_c)
print(literki(arr_a, arr_b, arr_c))
