import numpy as np
import matplotlib.pyplot as plt
import time

convex_points = []


def get_points():
    """
    随机获取15个点
    :return:
    """
    x = np.random.randint(low=-10, high=10, size=8)
    y = np.random.randint(low=-10, high=10, size=8)
    points = []
    for index in range(len(x)):
        point = [x[index], y[index]]
        points.append(point)
    return points


def solve(points):
    sorted_points = sort_points_by_x(points)
    dhull(sorted_points, 0, len(points) - 1)
    uhull(sorted_points, 0, len(points) - 1)


def get_distance(point1, point2, point3):
    """
    获得p3到p1\p2直线的距离
    :param points:
    :param point1:
    :param point2:
    :return:
    """
    return abs(
        (point2[1] - point1[1]) * point3[0]
        + (point1[0] - point2[0]) * point3[1]
        + (point1[0] - point2[0]) * point3[1]
        + (point1[1] - point2[1]) * point1[0]
        + (point2[0] - point1[0]) * point1[1]) / (pow(point2[1] - point1[1], 2)
                                                  + pow(point1[0] - point2[0], 2)) ** 2


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


def multi(point1, point2, point3):
    """
    判断p3在point1p2的左方还是右方
    :param point1:
    :param point2:
    :param point3:
    :return:
    """
    return point1[0] * point2[1] + point3[0] * point1[1] + point2[0] * point3[1] - point3[0] * point2[1] - point2[0] * \
           point1[1] - point1[0] * point3[1]


def dhull(points, x, y):
    dis = -1
    farthest = -1
    if x <= y:
        star = x
        end = y
    else:
        star = y
        end = x
    for index in range(star + 1, end):
        if multi(points[x], points[y], points[index]) <= 0:
            if get_distance(points[x], points[y], points[index]) > dis:
                dis = get_distance(points[x], points[y], points[index])
                farthest = index
    if farthest < 0:
        if points[x] not in convex_points:
            convex_points.append(points[x])
        if points[y] not in convex_points:
            convex_points.append(points[y])
        draw(convex_points, points)
        return
    if multi(points[x], points[farthest], points[y]) <= 0:
        uh = x
        dh = y
    else:
        uh = y
        dh = x
    dhull(points, dh, farthest)
    uhull(points, uh, farthest)


def uhull(points, x, y):
    dis = -1
    farthest = -1
    if x <= y:
        star = x
        end = y
    else:
        star = y
        end = x
    for index in range(star + 1, end):
        if multi(points[x], points[y], points[index]) >= 0:
            if get_distance(points[x], points[y], points[index]) > dis:
                dis = get_distance(points[x], points[y], points[index])
                farthest = index
    if farthest < 0:
        if points[x] not in convex_points:
            convex_points.append(points[x])
        if points[y] not in convex_points:
            convex_points.append(points[y])
        draw(convex_points, points)
        return
    if multi(points[x], points[farthest], points[y]) <= 0:
        uh = x
        dh = y
    else:
        uh = y
        dh = x
    dhull(points, dh, farthest)
    uhull(points, uh, farthest)


def draw(margin_points, points):
    margin_x = [x[0] for x in margin_points]
    margin_y = [y[1] for y in margin_points]
    margin_x.append(margin_points[0][0])
    margin_y.append(margin_points[0][1])

    origin_x = [x[0] for x in points]
    origin_y = [y[1] for y in points]

    plt.scatter(origin_x, origin_y)
    plt.plot(margin_x, margin_y, color="R")
    time.sleep(1)
    plt.show()


if __name__ == "__main__":
    points = get_points()
    # points = [[1, -5], [5, -10], [-8, 1], [-5, 7], [-2, -9], [5, 7], [2, 5], [-10, 0]]
    print(points)
    solve(points)
    draw(convex_points, points)
    print(convex_points)
