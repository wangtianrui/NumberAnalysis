import numpy as np
import matplotlib.pyplot as plt


def get_points():
    x = [0, 1, 2, 4]
    y = [3, 6, 11, 51]
    return x, y


def draw(points_x, points_y, ks, pre_pointx):
    plt.scatter(points_x, points_y)
    x_temp = np.arange(start=0, stop=5, step=0.2)
    y_temp = []
    for i in range(len(x_temp)):
        y_temp.append(function(ks, points_x, x_temp[i]))
    plt.plot(x_temp, y_temp)
    plt.scatter(pre_pointx, function(ks, points_x, pre_pointx), color="R")
    plt.show()

def newton_interpolation(x, y):
    length = len(x)
    if length == 1:
        return y[0]
    else:
        k = (newton_interpolation(x[:-1], y[:-1])
             - newton_interpolation(x[1:], y[1:])) / (x[0] - x[-1])
        print("1607094155-王天锐")
        return k


def solve(x, y):
    ks = []
    for i in range(1, len(x) + 1):
        ks.append(newton_interpolation(x[:i], y[:i]))
        print(ks)
    return ks


def function(ks, xs, x):
    y = ks[0] + ks[1] * (x - xs[0]) + ks[2] * (x - xs[0]) * (x - xs[1]) + ks[3] * (x - xs[0]) * (x - xs[1]) * (
            x - xs[2])
    print(ks, "1607094155-王天锐")
    return y


if __name__ == "__main__":
    x, y = get_points()
    k = solve(x, y)
    draw(points_x=x, points_y=y, ks=k, pre_pointx=0.5)
