def przedzial(A,t):
    n = len(A)
    A.sort()
    res = 0
    for i in range(n-t+1): #wybieram od ktorego klocka zaczynam
        ctr = 1
        tab = [i]
        j = i+1
        end = A[i][1]
        end2 = end
        while ctr != t:
            while j<n and A[j][0] < end:
                if A[j][1] > end2:
                    end2 = A[j][1]
                    ans = j
                j+=1
            tab.append(ans)
            end = end2
            ctr += 1
        print(i,end-A[i][0])
        if end-A[i][0] > res:
            res = end-A[i][0]
            hehe = tab
    return hehe,res

A = [[1, 8], [4, 14], [7, 11], [10, 14], [13, 19], [18, 22], [21, 24], [23, 26]]

print(przedzial(A,4))
