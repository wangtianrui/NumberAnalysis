import matplotlib.pyplot as plt
import numpy as np
import time

"""
凸包问题  ——蛮力法以及求解过程点的可视化（可视化内含一秒延时）    
2018-11-28 by 王天锐
"""


def get_points():
    """
    随机获取15个点
    :return:
    """
    x = np.random.randint(low=-10, high=10, size=15)
    y = np.random.randint(low=-10, high=10, size=15)
    points = []
    for index in range(len(x)):
        point = [x[index], y[index]]
        points.append(point)
    return points


def solve(points):
    """
    求解过程
    :param points:
    :return:
    """
    out_margin_points = []
    for i in range(len(points)):
        point1 = points[i]
        for j in range(i + 1, len(points)):
            margin = []
            point2 = points[j]
            kb = get_kb(point1, point2)
            for index in range(len(points)):
                if index == i or index == j:
                    continue
                point_test = np.array(points[index])
                if len(kb) == 1:
                    diff = (point_test[kb[0]] - point2[kb[0]])
                    if diff != 0:
                        margin.append(diff)
                else:
                    pre = calculate(point_test, kb)
                    diff = pre - point_test[1]
                    if diff != 0:
                        margin.append(diff)
            margin = np.array(margin)
            above_zero = (margin >= 0).astype(int)
            print(point1, point2, above_zero)
            if above_zero.sum() == len(above_zero) or above_zero.sum() == 0:
                if point1 not in out_margin_points:
                    out_margin_points.append(point1)
                    draw(out_margin_points, points)
                if point2 not in out_margin_points:
                    out_margin_points.append(point2)
                    draw(out_margin_points, points)

    return out_margin_points


def get_kb(point1, point2):
    """
    通过两点获得斜率
    :param point1:
    :param point2:
    :return:
    """
    a = [[point1[0], 1], [point2[0], 1]]
    b = [point1[1], point2[1]]
    if point1[0] == point2[0]:
        kb = [0]
    elif point1[1] == point2[1]:
        kb = [1]
    else:
        kb = np.linalg.solve(
            np.array(a),
            np.array(b)
        )
    return np.array(kb)


def calculate(points, kb):
    """
    带入直线计算得y
    :param points:
    :param kb:
    :return:
    """
    return points[0] * kb[0] + kb[1]


def draw(margin_points, points):
    """
    可视化，内含一秒延时操作
    :param margin_points:
    :param points:
    :return:
    """
    margin_x = [x[0] for x in margin_points]
    margin_y = [y[1] for y in margin_points]

    origin_x = [x[0] for x in points]
    origin_y = [y[1] for y in points]
    plt.scatter(origin_x, origin_y)
    plt.scatter(margin_x, margin_y, color="R")
    plt.show()
    time.sleep(1)
    plt.close()


if __name__ == "__main__":
    points = get_points()
    print(points)
    margin_points = solve(points)
    print(margin_points)
