def solution(A):
    len_slice = len(A) - 2
    min_average = (A[0] + A[1]) / 2
    min_index = 0
    average_3 = (A[-1] + A[-2]) / 2

    for i in range(len_slice):
        average_1 = (A[i] + A[i + 1]) / 2
        average_2 = (A[i] + A[i + 1] + A[i + 2]) / 3

        if average_1 < min_average:
            min_average = average_1
            min_index = i
        elif average_2 < min_average:
            min_average = average_2
            min_index = i

    if average_3 < min_average:
        min_index = len_slice

    return min_index


# test
B = [4, 2, 2, 5, 1, 5, 8]
print(solution(B))
