import matplotlib.pyplot as plt
import numpy as np
import time

"""
最近点对问题  ——蛮力法以及求解过程点的可视化（可视化内含一秒延时）
2018-11-28 by 王天锐
"""


def get_points():
    """
    随机获取13个点，由于后面颜色的数量有限，所以必须13个点以内
    :return:
    """
    x = np.random.randint(low=1, high=20, size=13)
    y = np.random.randint(low=2, high=18, size=13)
    points = []
    plt.scatter(x, y)
    plt.show()
    # plt.scatter(x)
    for index in range(len(x)):
        point = [x[index], y[index]]
        points.append(point)
    return points


def get_distance(point1, point2):
    """
    获取两点距离： dis = ((y1-y2)**2 + (x1-x2)**2)**0.5
    :param point1:
    :param point2:
    :return:
    """
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.sum((point2 - point1) ** 2) ** 0.5
    return distance


def solve(points):
    """
    求解问题以及可视化
    :param points:
    :return:
    """
    result = []
    for i in range(len(points)):
        min_dis = 1000
        point1 = points[i]
        min_couple = []
        for j in range(len(points)):
            if i == j:
                continue
            point2 = points[j]
            dis = get_distance(point1, point2)
            if min_dis >= dis:
                min_dis = dis
                if len(min_couple) != 0:
                    min_couple.pop()
                min_couple.append((point1, point2))
        result.append(min_couple)
        draw(result, points, point1)
    return result


def draw(couples, points, target_point):
    """
    可视化，内含一秒延时，求解点不能超过 colors 数组的size
    :param couples:
    :param points:
    :param target_point:
    :return:
    """
    colors = [
        'darkgoldenrod', 'darkgray',
        'darkgreen', 'darkkhaki',
        'darkmagenta', 'darkolivegreen',
        'darkorange', 'darkorchid',
        'darkred', 'darksalmon',
        'darkseagreen', 'darkslateblue', 'darkslategray']
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)
    plt.scatter(target_point[0], target_point[1], color="R")
    for index in range(len(couples)):
        points1 = couples[index][0][0]
        points2 = couples[index][0][1]

        xs = [points1[0], points2[0]]
        ys = [points1[1], points2[1]]
        plt.plot(xs, ys, color=colors[index])
    plt.show()
    time.sleep(1)
    plt.close()


def solve_(points):
    min_couple = []
    diff = 100
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            temp_diff = get_distance(points[i], points[j])
            if diff >= temp_diff:
                diff = temp_diff
                if len(min_couple) != 0:
                    min_couple.pop()
                min_couple.append([points[i], points[j]])
                print("当前最近点对为：", min_couple)
                draw_(min_couple, points)


def draw_(couple, points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)

    points1 = couple[0][0]
    points2 = couple[0][1]
    xs = [points1[0], points2[0]]
    ys = [points1[1], points2[1]]
    plt.plot(xs, ys, color="R")
    time.sleep(1)
    plt.show()


if __name__ == "__main__":
    points = get_points()
    points = [[1, -5], [5, -10], [-8, 1], [-5, 7], [-2, -9], [5, 7], [2, 5], [-10, 0]]
    couples = solve_(points)
