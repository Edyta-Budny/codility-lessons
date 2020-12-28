def solution(A):
    unique_A = set(A)
    len_A = len(unique_A)
    i = 1

    for element in range(len_A + 1):
        if i not in unique_A:
            return i
        else:
            i += 1


# test
B = [1, 3, 6, 4, 1, 2]
C = [1, 2, 3]
D = [-1, -3]
E = [-1, -3, 1, 2]
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
