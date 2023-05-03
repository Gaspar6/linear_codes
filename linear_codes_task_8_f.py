import random

from scipy.spatial.distance import hamming


def minimize_hamming_distance(B, C, v, k):

    # finding m
    current_min = float('inf')
    for w in C:
        dist = hamming(v,w)
        if dist < current_min:
            current_min = dist
    m = current_min

    # finding L
    L = []
    for w in C:
        if hamming(w, v) == m:
            L.append(w)

    # finding w
    w = L[random.randint(0, len(L)-1)]
    print("w:")
    print(w)
    # finding r
    Z_k = [ i for i in range(k)]
    r = (0,0,0)

    for a in Z_k:
        for b in Z_k:
            for c in Z_k:
                for d in Z_k:

                    vector = []
                    for i in range(len(B[0])):
                        vector.append( a * B[0][i] + b * B[1][i] + c * B[2][i] + d * B[3][i])
                    for i in range(len(vector)):
                        vector[i] = vector[i] % k


                    if vector == w:
                        return [a, b, c, d]

def linear_combination(base, k):
    # all linear combinations of vectors from base in field Zk

    Z_k = [ i for i in range(k)]
    result = []

    for a in Z_k:
        for b in Z_k:
            for c in Z_k:
                for d in Z_k:

                    vector = []

                    for i in range(len(base[0])):
                        vector.append( a * base[0][i] + b * base[1][i] + c * base[2][i] + d * base[3][i])

                    for i in range(len(vector)):
                        vector[i] = vector[i] % k
                    if vector not in result:
                        result.append(vector)
    return result


def same(A, B):
    result = []
    for i in range(len(A)):
        if A[i] == B[i]:
            result.append(True)
        else:
            result.append(False)
    return result





if __name__ == '__main__':

    B = [[1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1],
     [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0],
     [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1],
     [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]]

    C = linear_combination(B, 5)

    print("C:")
    print(C)

    X = [[4, 2, 2, 4, 2, 0, 1, 2, 3, 2], [3, 1, 3, 1, 1, 1, 4, 2, 2, 1], [0, 4, 2, 3, 0, 2, 1, 0, 0, 3], [0, 0, 4, 2, 4, 4, 2, 4, 3, 0], [0, 0, 4, 2, 1, 4, 2, 4, 3, 0], [3, 4, 1, 0, 1, 2, 1, 2, 3, 2], [1, 3, 3, 1, 3, 0, 4, 1, 2, 3], [4, 0, 3, 3, 1, 4, 1, 2, 0, 4], [1, 1, 0, 3, 1, 0, 2, 0, 1, 0], [0, 2, 3, 4, 4, 0, 2, 3, 4, 1], [4, 1, 1, 2, 0, 2, 2, 4, 3, 0]]

    XT = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
    print(XT)

    R_matrix = []
    for v in XT:
        R_matrix.append(minimize_hamming_distance(B, C, v, 5))

    print("r matrix")
    print(R_matrix)
    RT = [[R_matrix[j][i] for j in range(len(R_matrix))] for i in range(len(R_matrix[0]))]

    print(RT)

    AT = [[4, 3, 0, 0], [2, 1, 4, 0], [2, 0, 4, 4], [4, 1, 3, 2], [2, 1, 0, 1], [0, 1, 2, 4], [1, 4, 1, 2], [4, 2, 0, 4], [3, 2, 0, 3], [2, 1, 3, 0]]
    print("are same???")
    print(same(AT, R_matrix))





