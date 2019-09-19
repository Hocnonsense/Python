# -*- coding: utf-8 -*-

"""
    计算从 n个数中挑选 k个数的所有可能的组合
    使用回溯法
    时间复杂度: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!)))
"""


def 生成所有组合(n: int, k: int) -> [[int]]:
    """
    >>> 生成所有组合(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    
    结果 = list()
    __生成所有组合(0, n, k, 结果)
    return 结果


def __生成所有组合(当前数, 总数, 空位, 结果, 当前组合 = list()):
    if 空位 == 0:
        结果.append(当前组合[:])  #使其作为一个列表加入新列表
    else:
        for i in range(当前数, 总数 - 空位 + 1): # 对于每一层, 都要保证剩下的空位可以被占满, 所以最多可以从 (总数-空位) 个中选取一个. 
            当前组合.append(i)
            __生成所有组合(i + 1, 总数, 空位 - 1, 结果, 当前组合)
            当前组合.pop()


def 输出结果(结果):
    for i in 结果:
        print(*i)   # 输出 list 中的内容而非 list 本身


if __name__ == '__main__':
    n, k = 5, 3
    结果 = 生成所有组合(n, k)
    输出结果(结果)

