import math


def solution(X, Y, D):
    if X and Y and D > 0:
        min_num_of_jumps = math.ceil((Y - X)/D)
    return min_num_of_jumps


# test
A = 10
B = 85
C = 30
print(solution(A, B, C))
