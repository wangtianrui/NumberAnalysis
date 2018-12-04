import numpy as np

"""
贪心算法 —— 背包问题   by 王天锐 2018/12/04
"""


def solve(values, weights, bag_max):
    values = np.array(values)
    weights = np.array(weights)
    unit_values = values / weights
    now_weight = 0
    now_choice = np.zeros(len(values))
    while now_weight < bag_max:
        rest = bag_max - now_weight
        max_index = np.argmax(unit_values)
        if np.sum(unit_values) != 0:
            if rest >= weights[max_index]:
                now_weight += weights[max_index]
                now_choice[max_index] = weights[max_index]
                unit_values[max_index] = 0
            else:
                now_choice[max_index] = rest
                break
        else:
            break
    now_choice = np.array(now_choice)
    sum_value = np.sum((now_choice > 0) * values)
    return now_choice, sum_value


if __name__ == "__main__":
    values = [1, 5, 3, 10, 3]
    weights = [6, 8, 6, 6, 7]
    bag_max = 12
    choice, value_sum = solve(values, weights, bag_max)
    print(values)
    print(weights)
    print(choice)
    print("总价值为", value_sum)
