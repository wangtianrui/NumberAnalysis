import numpy as np
import matplotlib.pyplot as plt
import copy


def get_parameters(random=False):
    if random:
        a = np.random.randint(low=-100, high=100, size=(4, 4))
        b = np.random.randint(low=-50, high=50, size=(4, 1))
    else:
        a = [[1, 2, -3],
             [0, 5, 2],
             [-2, 0, -3]]
        b = [[8], [-4], [2]]
    return a, b


def exchange_principal_component(a, b, starrow=0):
    a = np.array(a)
    first_row = a[starrow]
    for index in range(len(first_row)):
        column = abs(np.array([item[0] for item in a]))
        average = abs(np.mean(column))
        index_item = abs(first_row[index])
        # print(index_item, average)
        if index_item < 1e-2 and (average > index_item):
            max_index_column = np.argmax(column)
            temp = copy.copy(a[index])
            a[index] = a[max_index_column]
            a[max_index_column] = temp
            temp = b[index]
            b[index] = b[max_index_column]
            b[max_index_column] = temp
            break
    return a, b


def solve(a, b):
    a, b = exchange_principal_component(a, b)
    b = np.reshape(b, (len(b), 1))
    merge = np.column_stack((a, b))
    merge = np.array(merge, dtype=float)
    print("增广矩阵为")
    print(merge)
    for row in range(0, len(a) - 1):
        for row_item in range(row + 1, len(a)):
            if merge[row_item][row] == 0:
                continue
            else:
                factor = merge[row_item][row] / merge[row][row]
            merge[row_item] -= factor * merge[row]
    print("消去法后的增广矩阵为")
    print(merge)
    xs = np.zeros(shape=(len(merge)))
    for row_index in reversed(range(len(merge))):
        print("1607094155-王天锐")
        sum = 0
        sum_index = row_index + 1
        while sum_index < len(xs):
            sum += merge[row_index][sum_index] * xs[sum_index]
            sum_index += 1
        xs[row_index] = (merge[row_index][-1] - sum) / merge[row_index][row_index]
    print("解是", xs)


if __name__ == "__main__":
    a, b = get_parameters()
    solve(a, b)
