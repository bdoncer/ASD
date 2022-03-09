def dlugosc(a):
    dl = 0
    while a != 0:
        dl += 1
        a = a//10
    return dl
def ktory_wiekszy(a,b):
    first = a*pow(10,dlugosc(b))+b
    second = b*pow(10,dlugosc(a))+a
    return first >= second

def merge(T, left, middle, right):
    pom1 = [0] * (middle - left + 1)
    pom2 = [0] * (right - middle)
    j = left
    for i in range(len(pom1)):
        pom1[i] = T[j]
        j += 1
    j = middle + 1
    for i in range(len(pom2)):
        pom2[i] = T[j]
        j += 1
    finger1 = 0
    finger2 = 0
    index = left
    while finger1 < len(pom1) and finger2 < len(pom2):
        if not ktory_wiekszy(pom1[finger1],pom2[finger2]):
            T[index] = pom1[finger1]
            index += 1
            finger1 += 1
        else:
            T[index] = pom2[finger2]
            index += 1
            finger2 += 1
    while finger2 < len(pom2):
        T[index] = pom2[finger2]
        index += 1
        finger2 += 1
    while finger1 < len(pom1):
        T[index] = pom1[finger1]
        index += 1
        finger1 += 1

def MergeSort(T, left, right):
    if left >= right:
        return
    middle = (right + left) // 2
    MergeSort(T, left, middle)
    MergeSort(T, middle + 1, right)
    merge(T, left, middle, right)

def largest_number_possible(T):
    MergeSort(T,0,len(T)-1)
    T.reverse()
    print(T)


T=[10, 68, 97, 9, 21, 12]
largest_number_possible(T)