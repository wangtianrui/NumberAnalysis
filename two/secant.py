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
        return abs(x_new - x_old) / abs(x_new)


def double_secant(x, x_old):
    """
    双点弦截法
    x_new = xk - (f(xk) / (f(xk)-f(xk-1))) * (f(xk) - f(x_old))
    :param x:
    :param x_old:
    :return:
    """
    x_new = x - (function(x) / (function(x) - function(x_old))) * (function(x) - function(x_old))
    x_old = x
    return x_new, x_old


def single_secant(x, x0):
    """
    单点弦截法
    x_new = xk - (f(xk) / (f(xk)-f(x0))) * (f(xk) - f(x0))
    :param x:
    :param x0:
    :return:
    """
    x_new = x - (function(x) / (function(x) - function(x0)))* (function(x) - function(x0))
    return x_new, x


def solveByDoubleSecant(a, b):
    """
    使用双点弦截法求解
    :param a:
    :param b:
    :return:
    """
    losses = []
    x_oldes = []
    lo = 1
    x_new = a
    x_old = b
    while lo > 1e-7:
        x_new, x_old = double_secant(x_new, x_old)
        x_oldes.append(x_old)
        lo = loss(x_new, x_old)
        losses.append(lo)
        print("双弦截法：loss:", lo)
    return np.array(x_oldes), np.array(losses)

def solveBySingleSecant(a, x0):
    """
    使用单点弦截法求解
    :param a:
    :param b:
    :return:
    """
    losses = []
    x_oldes = []
    lo = 1
    x_new = a
    while lo > 1e-7:
        x_new, x_old = single_secant(x_new, x0)
        x_oldes.append(x_old)
        lo = loss(x_new, x_old)
        losses.append(lo)
        print("单弦截法：loss:", lo)
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
    X,losses = solveByDoubleSecant(-10, 10)
    drawer(X,losses)
    print("\n\n")
    X, losses = solveBySingleSecant(-5, 10)
    drawer(X, losses)

