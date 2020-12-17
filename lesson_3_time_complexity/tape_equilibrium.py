def solution(A):
    N = len(A)
    first_part = A[0]
    second_part = sum(A[1:])
    min_difference = abs(first_part - second_part)

    for i in range(1, N - 1):
        first_part += A[i]
        second_part -= A[i]
        if abs(first_part - second_part) < min_difference:
            min_difference = abs(first_part - second_part)
    return min_difference


# test
B = [3, 1, 2, 4, 3]
print(solution(B))
