import numpy as np
import matplotlib.pyplot as plt


def function(x):
    """
    y = 2x^5 - 18x^4 - 2x^3 - 6x^2 + x + 3
    :param x:
    :return:
    """
    return 2 * x ** 5 - 18 * x ** 4 - 2 * x ** 3 - 6 * x ** 2 + x + 3


def draw():
    x_temp = np.arange(start=-100, stop=100, step=0.5)
    plt.plot(x_temp, function(x_temp))
    plt.show()


def get_loss(u, u_old, v, v_old):
    loss_u = abs(u - u_old) / abs(u)
    loss_v = abs(v - v_old) / abs(v)
    # print("u_loss:%0.9f,v_loss:%0.9f" % (loss_u, loss_v))
    return loss_u, loss_v


def get_new_uv(u, v, ans):
    """
    更新u,v
    :param u:
    :param v:
    :param ans:
    :return:
    """
    bns = get_b(u, v, ans)

    r0, r1 = -bns[-2], -bns[-1]
    # print(r0, r1)
    cns = get_c(bns, u, v)
    # print(bns)
    # print(cns)
    # if i == max_n - 2:
    #     cn = cn + u * cns[-1]
    # s0 = cns[-4]
    # s1 = cns[-3] + u*cns[-4]
    # dr0v = -s0
    # dr1v = -s1
    # # print(dr0v, dr1v)
    # dr0u = u * s0 - s1
    # dr1u = v * s0
    # print(cns)
    c1 = cns[-1]
    c2 = cns[-2]
    c3 = cns[-3]

    # du = (r1 - r0 * (dr0v / dr1v)) / (dr0u - dr1u) * 1e-3
    # dv = (r1 - dr0u * du) / dr0v * 1e-3
    # print(du, dv)
    x = np.linalg.solve(np.array([[c2, c3], [c1, c2]]), np.array([r0, r1]))
    du = x[0]
    dv = x[1]
    return u + du, v + dv


def get_b(u, v, ans):
    """
    获得b的所有值
    :param n:
    :param u:
    :param v:
    :param max_n:
    :return:
    """
    a = ans
    b0 = a[0]
    b1 = a[1] + u * a[0]
    bns = [b0, b1]

    i = 2
    bn_1 = b1
    bn_2 = b0
    max_n = len(a) - 1
    while i <= max_n:
        bn = a[i] + u * bn_1 + v * bn_2

        bns.append(bn)
        bn_2 = bn_1
        bn_1 = bn
        i += 1
    return bns


def get_c(bns, u, v):
    """
    获取所有的c
    :param bns:
    :param u:
    :param v:
    :param max_n:
    :return:
    """
    cns = []
    c0 = bns[0]
    c1 = bns[1] + u * c0
    cns.append(c0)
    cns.append(c1)
    i = 2

    max_n = len(bns) - 1
    while i <= max_n - 1:
        cn = bns[i] + u * cns[-1] + v * cns[-2]
        cns.append(cn)
        i += 1
    return cns


# [1, -3.5, 2.75, 2.125, -3.875, 1.25]
# ans=[2, -18, -2, -6, 1, 3]
def solve(u=-10, v=-5, ans=[1, -3.5, 2.75, 2.125, -3.875, 1.25]):
    temp = ans
    answers = set()
    f = np.poly1d(ans)

    while len(f.c) > 3:
        u_old, v_old = 10, 10
        loss_u, loss_v = get_loss(u, u_old, v, v_old)
        while loss_u > 1e-3 and loss_v > 1e-3:
            u_old, v_old = u, v
            u, v = get_new_uv(u, v, ans)
            loss_u, loss_v = get_loss(u, u_old, v, v_old)
        x1, x2 = get_answer(u, v)
        ans = ploynomial_division(ans, div_ans=[1, -u, -v]).c
        f = np.poly1d(ans)
        answers.add(x1)
        answers.add(x2)
        # print("u:%0.5f,v:%0.5f；所对应的解是" % (u, v), x1, x2)
    last_ans = f.c
    answers.add(-last_ans[1] / float(last_ans[0]))
    print(np.poly1d(temp), "所有的根为：", answers)
    return answers


def get_answer(u, v):
    # print(u, v)
    delta = u ** 2 + 4 * v
    if delta > 0:
        x1 = (u + delta ** 0.5) / 2.0
        x2 = (u - delta ** 0.5) / 2.0
    elif delta == 0:
        x1 = x2 = v / 2.0
    else:
        delta = abs(delta)
        x1 = (u + delta ** 0.5) / 2.0
        x2 = (u - delta ** 0.5) / 2.0
        x1 = str(x1) + 'i'
        x2 = str(x2) + 'i'
    return x1, x2


def ploynomial_division(ans, div_ans):
    y = np.poly1d(ans)
    ans_new = y / div_ans
    # print(ans_new)
    return ans_new[0]


def check_answer(answers):
    print("\n检验根的正确性：")
    for x in answers:
        if str(x).split(".")[1].isdigit():
            print(x, "  对应的函数值为：", function(x), "趋近于0")
        else:
            print(x, "是复数根")


if __name__ == "__main__":
    # 默认函数为  y = 2x^5 - 18x^4 - 2x^3 - 6x^2 + x + 3
    ans = [2, -18, -2, -6, 1, 3]
    answers = solve(ans=ans)
    check_answer(answers)
