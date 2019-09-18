# 牛顿-拉夫逊(Newton Raphson)方法
# Author: Syed Haseeb Shah (github.com/QuantumNovice)

from decimal import Decimal # 为了提高精度, 以十进制形式存储数字

def 牛顿拉夫逊方法(表达式: str, 起始点, 变量名: str = "x", 精度: float = 10**-15):
    '''
        表达式应该是字符串形式的表达式, 其中可以且暂时只可以使用 sin 和 cos 函数
        变量名默认为 x
        使用牛顿-拉夫逊方法从起始点开始查找根
    '''
    表达式 = 表达式.replace(变量名, 'x')
    导数 = 求导(表达式)
    while True:
        from numpy import sin, cos
        x = 起始点
        新点 = Decimal(x) - ( Decimal(eval(表达式)) / Decimal(eval(导数)) )
        起始点 = float(新点)
        if abs(eval(表达式)) < 精度:
            return 新点

def 求导(原函数):
    """
        sympy 是一个形式化库, 可以对字符串形式的表达式求导, 其中可以且暂时只可以使用 sin 和 cos 函数
    """
    from sympy.abc import x
    from sympy import sin, cos, diff
    导数 = str(diff(原函数, x))
    return 导数

def exp(x):
    return pow(x, 3) - 2*x - 5

# Let's Execute
if __name__ == '__main__':
    # 找到三角函数的根, 比如说 numpy.pi
    print('sin(x) = 0  =>  x = ', 牛顿拉夫逊方法('sin(x)', 2, 'x'))

    # 求多项式的根
    print('x**2 - 5*x +2 = 0  =>  x = ', 牛顿拉夫逊方法('x**2 - 5*x +2', 0.4, 'x'))

    # 求平方根
    print('x**2 - 5 = 0  =>  x = ', 牛顿拉夫逊方法('x**2 - 5', 0.1, 'x'))

    # 求表达式的根, 似乎不符合语法
    #print('exp(x) - 1 = 0  =>  x = ', 牛顿拉夫逊方法('exp(x) - 1', 0, 'x'))
