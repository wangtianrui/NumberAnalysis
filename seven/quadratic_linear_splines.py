import numpy as np
import matplotlib.pyplot as plt


def get_points():
    points_num = 15
    x = range(points_num)
    y = np.random.randint(low=-5, high=5, size=points_num)
    points = []
    for index in range(len(x)):
        points.append([x[index], y[index]])
    return points


def quadratic_linear_splines(points):
    points = np.array(points)
    points_num, wid = points.shape
    ys = np.array([y[1] for y in points])
    xs = np.array([x[0] for x in points])
    x_2 = xs ** 2

    count = 3 * (points_num - 1)
    factors = np.zeros((count, count))

    y_s = [0]
    row = 1
    for index in range(1, points_num - 1):
        factors[row][(index - 1) * 3] = x_2[index]
        factors[row][(index - 1) * 3 + 1] = xs[index]
        factors[row][(index - 1) * 3 + 2] = 1
        y_s.append(ys[index])
        row += 1
        factors[row][(index) * 3] = x_2[index]
        factors[row][(index) * 3 + 1] = xs[index]
        factors[row][(index) * 3 + 2] = 1
        y_s.append(ys[index])
        row += 1
    factors[row][0] = x_2[0]
    factors[row][1] = xs[0]
    factors[row][2] = 1
    y_s.append(ys[0])
    row += 1
    factors[row][-1] = 1
    factors[row][-2] = xs[-1]
    factors[row][-3] = x_2[-1]
    y_s.append(ys[-1])
    row += 1
    for index in range(1, points_num - 1):
        factors[row][(index - 1) * 3] = 2 * xs[index]
        factors[row][(index - 1) * 3 + 1] = 1
        factors[row][(index - 1) * 3 + 2] = 0

        factors[row][index * 3] = -2 * xs[index]
        factors[row][index * 3 + 1] = -1
        factors[row][index * 3 + 2] = 0
        y_s.append(0)
        row += 1

    high = len(y_s)
    y_s = np.array(y_s).reshape(high, 1)

    factors = np.delete(factors, 0, axis=0)
    factors = np.delete(factors, 0, axis=1)
    y_s = np.delete(y_s, 0, axis=0)

    abcs = np.linalg.solve(factors, y_s)

    section = []

    index = 0
    while index < len(xs) - 1:
        section.append([xs[index], xs[index + 1]])
        index += 1
    return abcs, section


def draw(points, abcs, section):
    ys = [y[1] for y in points]
    xs = [x[0] for x in points]
    abcs = np.array(abcs)
    abcs = abcs.flatten()
    print(abcs)
    facters = []

    i = 0
    while i < len(abcs):
        if i == 0:
            facters.append([abcs[0], abcs[1]])
            i += 2
        else:
            facters.append([abcs[i], abcs[i + 1], abcs[i + 2]])
            i += 3
    # print(facters)

    for sect_index in range(len(section)):
        sect = section[sect_index]
        x_temp = np.arange(start=sect[0] - 0.1, stop=sect[1] + 0.2, step=0.2)
        y_temp = []
        for x in x_temp:
            if sect_index == 0:
                y_temp.append(function(facters[sect_index], x, True))
            else:
                y_temp.append(function(facters[sect_index], x, False))
        plt.plot(x_temp, y_temp)
        # print(y_temp)
    plt.scatter(xs, ys)
    plt.show()
    # print("1607094155-鐜嬪ぉ閿?)


def function(parameters, x, isA0=False):
    # print(parameters)
    if isA0:
        return parameters[0] * x + parameters[1]
    else:
        return parameters[0] * x ** 2 + parameters[1] * x + parameters[2]


if __name__ == "__main__":
    # points = [[3, 2.5], [4.5, 1], [7, 2.5], [9, 0.5]]
    points = get_points()

    abcs, section = quadratic_linear_splines(points)
    print(abcs)
    draw(points, abcs, section)
