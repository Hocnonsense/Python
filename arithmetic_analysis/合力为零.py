"""
检查一个在同一个平面上的力系是否处于静力平衡状态

python/black : true
flake8 : passed
mypy : passed
"""

from numpy import array, cos, sin, radians, cross  # type: ignore
from typing import List 


def 角坐标力(
    力的大小: float, 角度: float, 弧度: bool = False
) -> List[float]:
    """
    沿矩形分量分解力
    (力的大小, 角度) => (x分量, y分量)
    >>> 角坐标力(10, 45)
    [7.0710678118654755, 7.0710678118654755]
    >>> 角坐标力(10, 3.14, 弧度=True)
    [-9.999987317275394, 0.01592652916486828]
    """
    if 弧度:
        return [力的大小 * cos(角度), 力的大小 * sin(角度)]
    else:
        return [力的大小 * cos(radians(角度)), 力的大小 * sin(radians(角度))]


def 合力为零(
    力: array, 位置: array, eps: float = 10 ** -1
) -> bool:
    """
    检查系统是否处于平衡状态。它需要两个 numpy 数组对象。
    eps 指定精度
    力 ==>  [
                        [force1_x, force1_y],
                        [force2_x, force2_y],
                        ....]
    位置 ==>  [
                        [x1, y1],
                        [x2, y2],
                        ....]
    >>> force = array([[1, 1], [-1, 2]])
    >>> 位置 = array([[1, 0], [10, 0]])
    >>> 合力为零(force, 位置)
    False
    """
    # 计算力矩之和是否为零
    力矩: array = cross(位置, 力)    # 两个向量的叉乘, 运算结果是一个向量。此处计算每一对 (force_x*y - force_y*x)
    合力矩: float = sum(力矩)   # 
    return abs(合力矩) < eps


if __name__ == "__main__":
    # Test to check if it works
    力 = array(
        [
            角坐标力(718.4, 180 - 30),
            角坐标力(879.54, 45),
            角坐标力(100, -90)
        ])

    位置 = array([[0, 0], [0, 0], [0, 0]])

    assert 合力为零(力, 位置)   # assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

    # Problem 1 in image_data/2D_problems.jpg
    力 = array(
        [
            角坐标力(30 * 9.81, 15),
            角坐标力(215, 180 - 45),
            角坐标力(264, 90 - 30),
        ]
    )

    位置 = array([[0, 0], [0, 0], [0, 0]])

    assert 合力为零(力, 位置)

    # Problem in image_data/2D_problems_1.jpg
    力 = array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])

    位置 = array([[0, 0], [6, 0], [10, 0], [12, 0]])

    assert 合力为零(力, 位置)

    import doctest
    doctest.testmod()   # 测试一切以 ">>>" 开头的代码, 并和结果对比, 错误则报错
