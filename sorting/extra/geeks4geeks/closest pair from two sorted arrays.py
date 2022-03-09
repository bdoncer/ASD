from math import inf
def merge_two_arrays(pom1,pom2):
    finger1 = 0
    finger2 = 0
    index = 0
    T = [0]*(len(pom1)+len(pom2))
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
    return T

def closest_pair(A,B,x):
    T = merge_two_arrays(A,B)
    print(T)


closest_pair([1, 4, 5, 7],[10, 20, 30, 40],50)