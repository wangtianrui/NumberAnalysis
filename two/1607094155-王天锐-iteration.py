import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def function(x):
    """
    函数为  y = x - e^(-1)
    :param x:
    :return:
    """
    return x - np.exp(- x)


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


def iteration(x):
    """
    计算下一个x ，返回x_next以及x_old
    :param x:
    :return:
    """
    if function(x) != 0:
        return np.exp(- x), x
    else:
        return x, x


def solve(x):
    """
    求解
    :param x:
    :return:
    """
    losses = []
    X = []
    x_old = x + 1
    lo = loss(x, x_old)
    while lo > 1e-7:
        x, x_old = iteration(x)
        X.append(x_old)
        lo = loss(x, x_old)
        losses.append(lo)
        print("loss:", lo)
    return np.array(X), np.array(losses)


def drawer(X, losses):
    """
    可视化
    :param X:
    :param losses:
    :return:
    """
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title("求解过程")
    x_temp = np.arange(start=0, stop=1, step=0.01)
    y_temp = np.exp(- x_temp)
    scatters = np.exp(-X)
    plt.plot(x_temp, y_temp, color="G")
    plt.plot(x_temp, x_temp)
    plt.scatter(X, scatters, color="R")
    plt.scatter(X, X, color="R")

    plt.subplot(2, 1, 2)
    plt.title("loss")
    plt.plot(losses)
    plt.show()


if __name__ == "__main__":
    X, losses = solve(1)
    drawer(X, losses)
    print("一共求解了%d次，最终误差为%.10f" % (len(X), losses[-1]))
