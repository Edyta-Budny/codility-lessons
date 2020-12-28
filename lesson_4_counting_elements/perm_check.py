def solution(A):
    A.sort()
    i = 0

    if A[0] != 1:
        return 0

    while i < len(A) - 1:
        if A[i] == A[i + 1] - 1:
            i += 1
        else:
            return 0
    return 1


# test
B = [4, 1, 3, 2]
C = [4, 1, 3]
D = [2]
E = [1]
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
