import math


def 二分法(function, a, b):
    """
        用 bolzano 算法得到函数在 [a, b] 区间上的零点, 假设函数在该区间上单调且连续
    """
    start, end= a, b
    if function(a) == 0:  # 零点是 a 或 b
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:  # 区间两边同正或同负, 这个算法就不管用啦
        print("couldn't find root in [a,b]")
        return
    else:   # function(a) * function(b) < 0
        mid = (start + end) / 2.0
        while abs(start - mid) > 10**-7:  # 使精度达到 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid


def f(x):
    return math.pow(x, 3) - 2*x - 5

if __name__ == "__main__":
    print(二分法(f, 1, 1000))

