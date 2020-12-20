def solution(N, A):

    counters_value = [0] * N
    counter = 0
    max_counter = False

    for i in A:
        if i < N + 1:
            counters_value[i - 1] += 1
            counter = max(counters_value[i - 1],  counter)
            max_counter = False
        elif not max_counter:
            counters_value = [counter] * N
            max_counter = True
    return counters_value


# test
B = 5
C = [3, 4, 4, 6, 1, 4, 4]
print(solution(B, C))
