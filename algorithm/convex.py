import matplotlib.pyplot as plt
import numpy as np


def get_points():
    """
    随机获取15个点
    :return:
    """
    x = np.random.randint(low=1, high=20, size=15)
    y = np.random.randint(low=2, high=18, size=15)
    plt.scatter(x, y)
    plt.show()
    points = []
    for index in range(len(x)):
        point = [x[index], y[index]]
        points.append(point)
    return points


# def solve(points):
#     out_margin_points = []
#     flag = 0
#     for i in range(len(points)):
#         point1 = points[i]
#         for j in range(i + 1, len(points)):
#             point2 = points[j]
#             kb = get_kb(point1, point2)  # [k,b]
#             for index in range(len(points)):
#                 point_test = np.array(points[index])
#                 if len(kb) == 1:
#                     if point2[kb[0]] > point_test[kb[0]]:
#                         temp_flag = -1
#                     elif point2[kb[0]] < point_test[kb[0]]:
#                         temp_flag = 1
#                     else:
#                         temp_flag = flag
#                 else:
#                     y_pre = calculate(point_test, kb)
#                     if y_pre >= point_test[1]:
#                         temp_flag = -1
#                     else:
#                         # print("bu")
#                         temp_flag = 1
#                 if flag == 0:
#                     flag = temp_flag
#                 if flag * temp_flag >= 0:
#                     continue
#                 else:
#                     break
#             # print(index)
#             if index == len(points) - 1:
#                 if point1 not in out_margin_points:
#                     out_margin_points.append(point1)
#                 if point2 not in out_margin_points:
#                     out_margin_points.append(point2)
#             else:
#                 print(point2, "淘汰")
#                 if j == len(points) - 1:
#                     print(point1, "淘汰1")
#             flag = 0
#
#     return out_margin_points


def solve(points):
    out_margin_points = []
    for i in range(len(points)):
        point1 = points[i]
        for j in range(i + 1, len(points)):
            margin = []
            has_tent = []
            point2 = points[j]
            has_tent.append(point1)
            has_tent.append(point2)
            kb = get_kb(point1, point2)
            for index in range(len(points)):
                if points[index] in has_tent:
                    continue
                point_test = np.array(points[index])
                if len(kb) == 1:
                    margin.append((point_test[kb[0]] - point2[kb[0]]))
                else:
                    pre = calculate(point_test, kb)
                    margin.append(pre - point_test[1])
            margin = np.array(margin)
            above_zero = (margin >= 0).astype(int)
            if above_zero.sum() == len(above_zero) or above_zero.sum() == 0:
                # print(point2)
                if point1 not in out_margin_points:
                    out_margin_points.append(point1)
                if point2 not in out_margin_points:
                    out_margin_points.append(point2)
    return out_margin_points


def get_kb(point1, point2):
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
    return points[0] * kb[0] + kb[1]


def compare_2_points(point1, point2):
    if point1[0] == point2[0] and point1[1] == point2[1]:
        return True
    else:
        return False


def draw(margin_points, points):
    margin_x = [x[0] for x in margin_points]
    margin_y = [y[1] for y in margin_points]

    origin_x = [x[0] for x in points]
    origin_y = [y[1] for y in points]
    # plt.plot(margin_x,margin_y)
    plt.scatter(origin_x, origin_y)
    plt.scatter(margin_x, margin_y, color="R")
    plt.show()


if __name__ == "__main__":
    points = get_points()
    print(points)
    # points = [[15, 7], [1, 5], [3, 12], [15, 5], [9, 6], [12, 3], [5, 17], [7, 5], [5, 12], [10, 14], [12, 7], [1, 16],
    #           [18, 11], [14, 10], [5, 11]]
    # points = [[1, 2], [1, 3], [2, 4], [3, 4], [5, 6], [2, 3], [3, 1]]
    margin_points = solve(points)
    print(margin_points)
    draw(margin_points, points)
