import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def function(x):
    """
    函数为  y = e^(x/10) - 10
    :param x:
    :return:
    """
    y = np.exp(x / 10.0) - 10.0
    return y


def loss(x_new, x_old):
    """
    计算误差
    :param x_new:
    :param x_old:
    :return:
    """
    if x_new == 0:
        return abs(x_new - x_old)
    else:
        return abs(x_new - x_old) / x_new


def gradient(x):
    """
    求导
    :param x:
    :return:
    """
    return 0.2 * np.exp(x / 10.0)


def newtonGradient(x):
    """
    计算出新x，返回新x和旧x
    :param x:
    :return:
    """
    if function(x) == 0:
        return x, x
    else:
        x_new = x - (function(x) / gradient(x))
        return x_new, x


def solve(x):
    """
    求解
    :param x:
    :return:
    """
    losses = []
    x_oldes = []
    lo = 1
    while lo > 1e-7:
        x, x_old = newtonGradient(x)
        lo = loss(x, x_old)
        losses.append(lo)
        x_oldes.append(x_old)
        print("loss:", lo)
    return np.array(x_oldes), np.array(losses)


def drawer(X, losses):
    """
    可视化
    :param X:
    :param losses:
    :return:
    """
    x_temp = np.arange(-10, 35, step=0.1)
    plt.subplot(2, 1, 1)
    plt.title("求解过程")
    plt.plot(x_temp, function(x_temp))
    plt.scatter(X, function(X), color="R")
    plt.plot(x_temp, np.zeros(len(x_temp)), color="G")

    plt.subplot(2, 1, 2)
    plt.title("loss")
    plt.plot(range(len(losses)), losses)
    plt.show()


if __name__ == "__main__":
    x_oldes, losses = solve(5)
    drawer(x_oldes, losses)
