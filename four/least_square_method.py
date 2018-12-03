import numpy as np
import matplotlib.pyplot as plt


def get_points():
    points = [[0.0, 0.9], [0.2, 1.9], [0.4, 2.8], [0.6, 3.3], [0.8, 4.2]]
    return points


def function(x, kb):
    y = kb[0] + x * kb[1]
    return y


def lsm(points):
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    xs = np.array(xs)
    ys = np.array(ys)
    segma_y = np.sum(ys)
    segma_x = np.sum(xs)
    segma_1 = len(points)
    segma_x_2 = np.sum(xs ** 2)
    segma_x_y = np.sum(xs * ys)
    result = np.linalg.solve(
        a=[[segma_1, segma_x], [segma_x, segma_x_2]],
        b=[segma_y, segma_x_y]
    )
    return result


def draw(points, kb=[0.0, 0.0]):
    xs = [x[0] for x in points]
    ys = [x[1] for x in points]
    plt.scatter(xs, ys)

    x_test = np.arange(start=-0.1, stop=1.0, step=0.02)
    y_preds = function(x_test, kb)
    plt.plot(x_test, y_preds)
    plt.show()


if __name__ == "__main__":
    # print("hello")
    points = get_points()
    draw(points)
    kb = lsm(points)
    draw(points, kb)
