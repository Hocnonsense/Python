"""牛顿法"""

# 牛顿法 参见 - https://baike.baidu.com/item/%E7%89%9B%E9%A1%BF%E8%BF%AD%E4%BB%A3%E6%B3%95/10887580?fr=aladdin

# 原函数即 f(x), 导数即 f'(x)
def 牛顿法(原函数, 导数, 起始点, 精度: float = 10**-5):
    x_n = 起始点
    while True:
        x_n1 = x_n - 原函数(x_n) / 导数(x_n)
        if abs(x_n - x_n1) < 精度:
            return x_n1
        else:
            x_n = x_n1


def f(x):
    return (x**3) - (2 * x) - 5


def f1(x):
    return 3 * (x**2) - 2


if __name__ == "__main__":
    print(牛顿法(f, f1, 3))
