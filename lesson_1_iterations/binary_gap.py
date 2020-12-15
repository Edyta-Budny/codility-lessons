def solution(N):
    if N > 0:
        binary_representation = bin(N)[2:]
        list_of_elements = binary_representation.split('1')
        longest_binary_gap = 0
        if binary_representation.endswith('0'):
            selected_elements = list_of_elements[:-1]
        else:
            selected_elements = list_of_elements

        for element in selected_elements:
            if longest_binary_gap < len(element):
                longest_binary_gap = len(element)
        return longest_binary_gap


# test
A = 9
B = 529
C = 32
D = 6
E = 328
print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))
print(solution(E))
