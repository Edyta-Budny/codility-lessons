def solution(X, A):
    unique_A = set()
    for i in range(len(A)):
        unique_A.add(A[i])
        if len(unique_A) == X:
            return i
    return -1


# test
B = [1, 3, 1, 4, 2, 3, 5, 4]
D = [3]
C = 5
print(solution(C, B))
print(solution(C, D))
