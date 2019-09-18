import math

def 内插法(function,x0,x1):
    """
        求函数在给定区间附近的某一个零点
    """
    x_n, x_n1 = x0, x1
    while True:
        x_n2 = x_n1-(function(x_n1)/((function(x_n1)-function(x_n))/(x_n1-x_n)))
        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        else:
            x_n, x_n1=x_n1, x_n2

def f(x):
    return math.pow(x , 3) - (2 * x) -5

if __name__ == "__main__":
    print(内插法(f,3,3.5))
