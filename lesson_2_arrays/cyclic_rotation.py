def solution(A, K):
    if len(A) != 0:
        for x in range(1, K + 1):
            A.insert(0, A[-1])
            A.pop(-1)
        return A
    else:
        return A


# test
A = [1, 2, 3, 4, 5, 6]
B = []
K = 3
print(solution(A, K))
print(solution(B, K))
