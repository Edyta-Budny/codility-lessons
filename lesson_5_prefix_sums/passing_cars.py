def solution(A):
    len_A = len(A)
    index_list = []
    east_cars = A.count(0)
    pairs = 0

    for i in range(len_A):
        if A[i] == 0:
            index_list.append(i)

    for i in range(len(index_list)):
        pairs += (len_A - 1) - index_list[i] - (east_cars - 1)
        east_cars -= 1
        if pairs > 1000000000:
            pairs = -1
            break
    return pairs


# test
B = [0, 1, 0, 1, 1]
print(solution(B))
