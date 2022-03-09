def partition(T, right, left):
    lower = right
    equal = right
    bigger = left
    pivot = T[left]

    while equal <= bigger:
        if T[equal] < pivot:
            T[equal], T[lower] = T[lower], T[equal]
            equal += 1
            lower += 1
        if T[equal] > pivot:
            T[equal], T[bigger] = T[bigger], T[equal]
            bigger -= 1
        if T[equal] == pivot:
            equal += 1
    return lower, bigger


def sort(T, left, right):
    while left < right:
        border,bigger = partition(T, left, right)
        if border - left < right - bigger:
            sort(T, left, border - 1)
            left = bigger + 1
        else:
            sort(T, bigger + 1, right)
            right = border - 1
from random import randint
test = [randint(0, 5) for i in range(1000000)]
sort(test,0, len(test)-1)
for i in range(len(test)-1):
    if test[i]>test[i+1]:
        print('debilu jeden')