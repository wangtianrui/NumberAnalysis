import numpy as np
import matplotlib.pyplot as plt


def get_question():
    a = [
        [2, 2, 3],
        [4, 7, 7],
        [-2, 4, 5]
    ]

    b = [
        [3],
        [1],
        [-7]
    ]
    a = [
        [2, 2, 3, 4],
        [2, 4, 9, 16],
        [4, 8, 24, 63],
        [6, 16, 51, 100]
    ]

    b = [
        [1],
        [1],
        [3],
        [-29]
    ]
    return a, b


def lu_elimination(a, b):
    size = len(a)
    L = np.zeros((size, size))
    U = np.zeros((size, size))
    for index in range(size):
        U[0][index] = a[0][index]
        if index > 0:
            L[index][0] = a[index][0] / U[0][0]
        L[index][index] = 1

    for r in range(1, size):
        print("1607094155王天锐")
        for i in range(r, size):
            U[r][i] = a[r][i]
            temp = a[i][r]
            for k in range(r):
                U[r][i] -= L[r][k] * U[k][i]
                temp -= L[i][k] * U[k][r]
            L[i][r] = temp / U[r][r]
    print("L:\n", L)
    print("U:\n", U)
    b = np.array(b)
    D = np.linalg.inv(L).dot(b)

    X = np.linalg.inv(U).dot(D)
    X = X.flatten()
    X = X[::-1]
    return X


if __name__ == "__main__":
    a, b = get_question()
    print("a:\n", a, "\nb:\n", b)
    X = lu_elimination(a, b)
    print("解为：", X)
