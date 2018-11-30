from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import time

min_couple = []


def nearest_dot(s):
    length = len(s)
    left = s[:(int)(length / 2)]
    right = s[(int)(length / 2):]
    mid_x = (left[-1][0] + right[0][0]) / 2.0
    if len(left) > 2:
        lmin = nearest_dot(left)
    else:
        lmin = left
    if len(right) > 2:
        rmin = nearest_dot(right)
    else:
        rmin = right

    if len(lmin) > 1:
        dis_1 = get_distance(lmin)
    else:
        dis_1 = float("inf")
    if len(rmin) > 1:
        dis_2 = get_distance(rmin)
    else:
        dis_2 = float("inf")

    d = min(dis_1, dis_2)
    mid_min = []
    for i in left:
        if mid_x - i[0] <= d:
            for j in right:
                if abs(i[0] - j[0]) <= d and abs(i[1] - j[1]) <= d:
                    if get_distance((i, j)) <= d:
                        mid_min.append([i, j])
    if len(mid_min) != 0:
        for i in mid_min:
            if len(min_couple) == 0:
                min_couple.append(i[0])
                min_couple.append(i[1])
            elif get_distance(min_couple) > get_distance(i):
                min_couple.pop()
                min_couple.pop()
                min_couple.append(i[0])
                min_couple.append(i[1])
            draw_(min_couple, points)
        return min_couple
    elif dis_1 > dis_2:
        return rmin
    else:
        return lmin


# 求点对的距离
def get_distance(min):
    return sqrt((min[0][0] - min[1][0]) ** 2 + (min[0][1] - min[1][1]) ** 2)


def get_points():
    """
    随机获取13个点，由于后面颜色的数量有限，所以必须13个点以内
    :return:
    """
    x = np.random.randint(low=1, high=20, size=12)
    y = np.random.randint(low=2, high=18, size=12)
    points = []
    plt.scatter(x, y)
    plt.show()
    # plt.scatter(x)
    for index in range(len(x)):
        point = [x[index], y[index]]
        points.append(point)
    return points


def sort_points_by_x(points):
    """
    按x轴排序
    :param points:
    :return:
    """
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i][0] > points[j][0]:
                temp = points[i]
                points[i] = points[j]
                points[j] = temp
            if points[i][0] == points[j][0]:
                if points[i][1] > points[j][1]:
                    temp = points[i]
                    points[i] = points[j]
                    points[j] = temp
    return points


def divide_conquer(points):
    points = sorted(points)
    nearest_dots = nearest_dot(points)
    print(nearest_dots)
    draw_(nearest_dots, points)


def draw_(couple, points):
    print(couple)
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)

    points1 = couple[0]
    points2 = couple[1]
    xs = [points1[0], points2[0]]
    ys = [points1[1], points2[1]]
    plt.plot(xs, ys, color="R")
    time.sleep(1)
    plt.show()


if __name__ == "__main__":
    points = get_points()
    # points = [(0, 1), (3, 2), (4, 3), (5, 1), (1, 2), (2, 1), (6, 2), (7, 2), (8, 3), (4, 5), (9, 0), (6, 4)]
    divide_conquer(points)
