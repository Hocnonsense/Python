import math

def intersection(function,x0,x1): # 函数是f,我们想要找到它的根,x0和x1是两个随机的起始点
    x_n = x0
    x_n1 = x1
    while True:
        x_n2 = x_n1-(function(x_n1)/((function(x_n1)-function(x_n))/(x_n1-x_n)))
        if abs(x_n2 - x_n1) < 10**-5:
            return x_n2
        x_n=x_n1
        x_n1=x_n2

def f(x):
    return math.pow(x , 3) - (2 * x) -5

if __name__ == "__main__":
    print(intersection(f,3,3.5))
