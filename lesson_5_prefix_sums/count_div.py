import math


def solution(A, B, K):
    return math.floor(B / K) - math.ceil(A / K) + 1


# test
C = 6
D = 11
E = 2
print(solution(C, D, E))


