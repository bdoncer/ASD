def ile_konczacych(A,T,ktory_przedluza,index):
    for i in range(index+1):
        if T[i] < T[index] and A[i] + 1 > A[index]:
            A[index] = A[i] + 1
            ktory_przedluza[index] = i

def najdluzszy_rosnacy(T):
    n = len(T)
    A = [1]*n
    ktory_przedluza = [-1]*n
    for i in range(n):
        ile_konczacych(A,T,ktory_przedluza,i)
    max = [0,-1]
    for i in range(n):
        if A[i] > max[0]:
            max[0] = A[i]
            max[1] = i
    print(print_solution(T,ktory_przedluza,max[1]))
    return max[0]
def print_solution(T,ktory_przedluza,i):
    if i < 0:
        return []
    return print_solution(T,ktory_przedluza,ktory_przedluza[i]) + [T[i]]



arr = [11, 1, 10, 4, 3, 2, 8, 7, 12, 6, 9, 5]
print(najdluzszy_rosnacy(arr))