import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']


def solpe(x):
    return -2 * x ** 3 + 12 * x ** 2 - 20 * x + 8.5


def origin_function(x):
    return -0.5 * x ** 4 + 4 * x ** 3 - 10 * x ** 2 + 8.5 * x + 1


def euler(y0=1, step=0.5, section=(0, 4)):
    ys = [y0]
    star, end = section
    # print(star, end)
    print("欧拉法,1607094155-王天锐")
    for x in np.arange(star, end, step=step):
        y_next = y0 + solpe(x) * step
        ys.append(y_next)
        y0 = y_next
    return ys


def huen(y0=1, step=0.5, section=(0, 4)):
    ys = [y0]
    star, end = section
    # print(star, end)
    print("秀恩法,1607094155-王天锐")
    for x in np.arange(star, end, step=step):
        y_next = y0 + (solpe(x) + solpe(x + step)) / 2.0 * step
        ys.append(y_next)
        y0 = y_next
    return ys


def drawer(euler, huen):
    length = len(euler)
    plt.figure()
    x_temp = np.arange(0, length * 0.5, 0.5)
    plt.subplot(1, 2, 1)
    plt.title("欧拉法")
    plt.plot(x_temp, euler)
    x_temp = np.arange(0, length * 0.5 - 0.5, step=0.1)
    plt.plot(x_temp, origin_function(x_temp))

    plt.subplot(1, 2, 2)
    plt.title("秀恩法")
    x_temp = np.arange(0, length * 0.5, 0.5)
    plt.plot(x_temp, huen)
    x_temp = np.arange(0, length * 0.5 - 0.5, step=0.1)
    plt.plot(x_temp, origin_function(x_temp))
    plt.show()


if __name__ == "__main__":
    euler_ys = euler()
    huen_ys = huen()
    drawer(euler_ys, huen_ys)
