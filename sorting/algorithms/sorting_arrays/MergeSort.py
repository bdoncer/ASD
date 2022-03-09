#stabilny
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
        if pom1[finger1] <= pom2[finger2]:
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

T = [10,5,8,4,9,2,6,8,24,45,76,356,354]
print(T)
MergeSort(T,0,len(T)-1)
print(T)








'''def merge(t,left,middle,right):
    new_t_len = right - left + 1
    new_t = [0]*new_t_len
    curr = left
    for i in range(len(new_t)):
        new_t[i] = t[curr]
        curr += 1
    print(new_t)
    finger1 = 0
    diff = middle - left
    new_middle = diff
    finger2 = new_middle + 1
    print(finger1,finger2)
    curr = left
    while finger1 <= new_middle and finger2 < len(new_t):
        if new_t[finger1] <= new_t[finger2]:
            t[curr] = new_t[finger1]
            finger1 += 1
        else:
            t[curr] = new_t[finger2]
            finger2 += 1
        curr += 1

    while finger1 <= new_middle:
        t[curr] = new_t[finger1]
        finger1 += 1

def MergeSort(t,left,right):
    if left >= right:
        return
    middle = int((left+right)/2)
    MergeSort(t,left,middle)
    MergeSort(t,middle+1,right)
    merge(t,left,middle,right)

def main(t):
    start = 0
    end = len(t) - 1
    MergeSort(t,start,end)
'''
