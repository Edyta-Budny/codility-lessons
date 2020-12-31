def solution(A):
    A.sort()
    max_triplet = max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
    return max_triplet


# test
B = [-3, 1, 2, -2, 5, 6]
print(solution(B))
