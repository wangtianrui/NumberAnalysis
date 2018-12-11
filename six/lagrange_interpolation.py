import numpy as np
import matplotlib.pyplot as plt
import copy


def get_points():
    x = range(8)
    y = np.random.randint(low=-5, high=5, size=8)
    points = []
    for index in range(len(x)):
        points.append([x[index], y[index]])
    return points


def lagrange_indetpolation(x, points):
    ys = [y[1] for y in points]
    xs = [x[0] for x in points]

    y_pre = 0
    xs = np.array(xs, dtype=float)
    ys = np.array(ys, dtype=float)

    for index in range(len(points)):
        temp = copy.deepcopy(xs)  # 引用问题。得用deepcopy
        temp[index] = x - 1.0
        dividend = np.prod(x - temp) * ys[index]  # 所有元素乘积
        # print(dividend)
        temp2 = copy.deepcopy(xs)
        temp2[index] -= 1
        denominator = np.prod(xs[index] - temp2)
        y_pre = y_pre + dividend / denominator
    print("1607094155-王天锐")
    return y_pre


def solve(points):
    ys = [y[1] for y in points]
    xs = [x[0] for x in points]
    x_temp = np.arange(start=0, stop=len(points) - 0.8, step=0.1)
    y_temp = [lagrange_indetpolation(x, points) for x in x_temp]
    plt.scatter(xs, ys)
    plt.plot(x_temp, y_temp)
    plt.show()


if __name__ == "__main__":
    points = get_points()
    solve(points)
