import math


def 二分法(原函数, a, b, 精度: float = 10**-7):
    """
        用 bolzano 算法得到函数在 [a, b] 区间上的零点, 假设函数在该区间上单调且连续
    """
    左界, 右界= a, b
    if 原函数(a) == 0:  # 零点是 a 或 b
        return a
    elif 原函数(b) == 0:
        return b
    elif 原函数(a) * 原函数(b) > 0:  # 区间两边同正或同负, 这个算法就不管用啦
        print("couldn't find root in [a,b]")
        return
    else:   # 原函数(a) * 原函数(b) < 0
        while abs(左界 - mid) > 精度:  # 使精度达到 10^-7
            mid = (左界 + 右界) / 2.0
            if 原函数(mid) == 0:
                return mid
            elif 原函数(mid) * 原函数(左界) < 0:
                右界 = mid
            else:
                左界 = mid
        return mid


def f(x):
    return math.pow(x, 3) - 2*x - 5

if __name__ == "__main__":
    print(二分法(f, 1, 1000))

