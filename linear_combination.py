def linear_combination(base, k):
    """

    :param base:
    :param k:
    :return: list of all linear combinations of vectors from base in field Z_k

    """

    Z_k = [ i for i in range(k)]
    result = []

    for a in Z_k:
        for b in Z_k:
            for c in Z_k:

                vector = []

                for i in range(len(base[0])):
                    vector.append( a * base[0][i] + b * base[1][i] + c * base[2][i])

                for i in range(len(vector)):
                    vector[i] = vector[i] % k
                if vector not in result:
                    result.append(vector)
    return result






if __name__ == '__main__':

    B = [[1, 0, 0, 2, 4], [0, 1, 0, 1, 0], [0, 0, 1, 5, 6]]
    k = 7

    lin_comb = linear_combination(B, k)
    print(lin_comb)
    print(len(lin_comb))

