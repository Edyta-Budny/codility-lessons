def solution(S, P, Q):

    min_factors = []

    for p, q in zip(P, Q):
        sequence = S[p:q+1]

        if 'A' in sequence:
            min_factors.append(1)
        elif 'C' in sequence:
            min_factors.append(2)
        elif 'G' in sequence:
            min_factors.append(3)
        elif 'T' in sequence:
            min_factors.append(4)

    return min_factors


# test
A = 'CAGCCTA'
B = [2, 5, 0]
C = [4, 5, 6]
print(solution(A, B, C))
