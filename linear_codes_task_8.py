import copy
import random


def z_n_field(X, n):
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] %= n
    return X

def generate(nrow, ncol):
    A = [[random.randint(0, 4) for i in range(ncol)] for j in range(nrow)]
    return A


def norm(M, k):
    X = copy.deepcopy(M)
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] /= k
    return X


def return_v(A, k):
    result = []
    for i in range(len(A)):
        result.append(A[i][k])
    return result


def code_v(v, G):
    result = [0 for i in range(len(G[0]))]
    for i in range(len(result)):
        value = 0
        for j in range(len(v)):
            value += v[j] * G[j][i]
        result[i] = value
    return result


def code_matrix(A, G):
    result = [[0 for i in range(len(A[0]))] for j in range(len(G[0]))]
    for k in range(len(result[0])):
        v = return_v(A, k)
        w = code_v(v, G)

        for i in range(len(result)):
            result[i][k] = w[i]
    return result

def send(M):
    result = copy.deepcopy(M)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if random.uniform(0,1) < 0.95:
                result[i][j] = result[i][j] % 5
            else:
                result[i][j] = (result[i][j] + 3) % 5
    return result


if __name__ == '__main__':
    print("Symulacja")

    random.seed(2137)

    # a
    A = generate(4, 10)
    print("wygenerowana macierz A:")
    for i in A:
        print(i)

    AT = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print("AT")
    print(AT)

    # b
    X = norm(A, 4)
    print("X = unormowana macierz A:")
    for i in X:
        print(i)

    # d
    print("wektor v:")
    v = return_v(A, 0)
    for i in range(len(v)):
        v[i] %= 5
    print(v)

    matrix_G = [[1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1],
                [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0],
                [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]]

    # d
    print("zakodowany wektor v")
    coded_v = code_v(v, matrix_G)
    for i in range(len(coded_v)):
        coded_v[i] %= 5
    print(coded_v)

    # e
    print()
    print("zakodowana macierz A")
    coded_A = z_n_field(code_matrix(A, matrix_G), 5)
    for i in coded_A:
        print(i)

    print("\n wysłana macierz A")
    sent_A = send(coded_A)
    for i in sent_A:
        print(i)

    print(sent_A)
