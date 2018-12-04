import numpy as np

"""
动态规划 —— 01背包问题   by 王天锐 2018/12/04
"""


def get_list(values, weights, bag_max):
    value_list = []
    zeros = np.zeros(bag_max + 1)
    value_list.append(zeros)
    for i in range(len(values)):
        temp = [0.0]
        for j in range(1, bag_max + 1):
            if j >= weights[i]:
                # print(value_list, i, j)
                temp.append(
                    max(
                        value_list[i - 1][j],
                        value_list[i - 1][j - weights[i]] + values[i]
                    )
                )
            else:
                temp.append(value_list[i - 1][j])
        if i != 0:
            value_list.append(temp)
    for i in value_list:
        for number in i:
            print("%3d" % number, end="")
        print("")
    print("最多可装%d" % value_list[-1][-1])


if __name__ == "__main__":
    values = [0, 2, 5, 3, 10, 4]
    weights = [0, 1, 3, 2, 6, 2]
    bag_max = 12
    get_list(values, weights, bag_max)
