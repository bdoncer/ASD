def find(A):
    S = [0 for _ in range(len(A) + 1)]
    B = [0 for _ in range(len(A) + 1)]
    S[0] = 1
    B[0] = 1
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j]:
                B[i] = max(B[i], S[j] + 1)
            if A[i] < A[j]:
                S[i] = max(S[i], B[j] + 1)
    res = 0
    for i in range(len(A)):
        if res < max(B[i], S[i]):
            res = max(B[i], S[i])
    return res


if __name__ == '__main__':
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]

    print("The length of the longest alternating subsequence is",
          find(A))
