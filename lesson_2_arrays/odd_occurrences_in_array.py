def solution(A):
    len_A = len(A)
    if len_A > 1:
        A.sort()
        i = 0
        while i < (len_A - 1):
            if A[i] == A[i + 1]:
                i = i + 2
            else:
                return A[i]
        else:
            return A[i]
    else:
        return A[0]


# test
A = [9, 3, 9, 3, 9, 7, 9]
B = [2, 2, 3, 3, 4]
C = [42]
print(solution(A))
print(solution(B))
print(solution(C))
