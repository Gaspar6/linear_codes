import copy
import random


def z_n_field(X, n):
    """
    :param X: matrix
    :param n: determines Z_n field
    :return: modified matrix, so that its elements belong to Z_n field
    """
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] %= n
    return X

def generate(nrow, ncol, a, b):
    """
    :return: matrix nrow by ncol, which elements are integers i: a <= i <= b
    """
    A = [[random.randint(a, b) for i in range(ncol)] for j in range(nrow)]
    return A


def norm(M, k):
    """
    :return: normalized matrix M in Z_(k+1) field
    """
    X = copy.deepcopy(M)
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] /= k
    return X


def return_v(A, k):
    """
    :param A: matrix
    :param k: number of desired matrix A column (counting from 0)
    :return: (k+1)-th column from matrix A
    """
    assert 0 <= k <= len(A[0]) - 1
    result = []
    for i in range(len(A)):
        result.append(A[i][k])
    return result


def code_v(v, G):
    """
    :param v: vector to be coded
    :param G: coding matrix
    :return: coded vector v
    """
    assert len(v) == len(G)
    result = [0 for i in range(len(G[0]))]
    for i in range(len(result)):
        value = 0
        for j in range(len(v)):
            value += v[j] * G[j][i]
        result[i] = value
    return result


def code_matrix(A, G):
    """
    :param A: matrix to be coded
    :param G: coding matrix
    :return: coded matrix A
    """
    result = [[0 for i in range(len(A[0]))] for j in range(len(G[0]))]
    for k in range(len(result[0])):
        v = return_v(A, k)
        w = code_v(v, G)

        for i in range(len(result)):
            result[i][k] = w[i]
    return result

def send(M, k):
    """
    :param M: matrix to be sent
    :param k: determines Z_k field
    :return: simulates a matrix transmission with disturbances (5/100 chance that 3 will be modulo k added)
    """
    result = copy.deepcopy(M)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if random.uniform(0,1) < 0.95:
                result[i][j] = result[i][j] % k
            else:
                result[i][j] = (result[i][j] + 3) % k
    return result


if __name__ == '__main__':
    """
    simulation 
    """
    random.seed(2137)

    # a
    A = generate(4, 10, 0, 4)
    print("generating A:")
    for i in A:
        print(i)

    AT = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print("AT")
    print(AT)

    # b
    X = norm(A, 4)
    print("X = normalized A:")
    for i in X:
        print(i)

    # d
    print("vector v:")
    v = return_v(A, 0)
    for i in range(len(v)):
        v[i] %= 5
    print(v)

    matrix_G = [[1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1],
                [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0],
                [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]]

    # d
    print("coded wektor v")
    coded_v = code_v(v, matrix_G)
    for i in range(len(coded_v)):
        coded_v[i] %= 5
    print(coded_v)

    # e
    print()
    print("coded matrix A")
    coded_A = z_n_field(code_matrix(A, matrix_G), 5)
    for i in coded_A:
        print(i)

    print("\n sent matrix A")
    sent_A = send(coded_A)
    for i in sent_A:
        print(i)

    print(sent_A)
