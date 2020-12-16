def solution(A):
    len_A = len(A)
    if len(set(A)) == len_A:
        if len_A < 1:
            return 1
        else:
            A.sort()
            i = 0
            while i < len_A:
                if A[i] == A[-1] and A[0] == 1:
                    return A[i] + 1
                elif A[i] == A[-1]:
                    return A[0] - 1
                elif A[i] == A[i + 1] - 1:
                    i = i + 1
                else:
                    return A[i] + 1


# test
B = [2, 3, 1, 5]
C = []
D = [1, 3, 2, 4]
E = [1, 1, 3, 4, 5]
F = [2]
G = [1]
H = [2, 3]
J = [3, 4]
K = [3, 5]
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
print(solution(F))
print(solution(G))
print(solution(H))
print(solution(J))
print(solution(K))
