"""
    在线性代数中， LU分解(LU Decomposition)是矩阵分解的一种，可以将一个矩阵分解为一个单位下三角矩阵和一个上三角矩阵的乘积（有时是它们和一个置换矩阵的乘积）。LU分解主要应用在数值分析中，用来解线性方程、求反矩阵或计算行列式。

    菜鸡表示没读懂, 而且结果好像也不太对
"""

# lower–upper (LU) decomposition - https://en.wikipedia.org/wiki/LU_decomposition
import numpy


def LU分解(矩阵):
    """
        矩阵: 必须是 n阶
    """
    行, 列 = numpy.shape(矩阵)
    if 行 != 列: # 检查是否是 n阶矩阵
        return []
    else:
        L = numpy.zeros((行, 列))
        U = numpy.zeros((行, 列))
        for i in range(列):
            for j in range(i - 1):
                和 = 0
                for k in range(j - 1):
                    和 += L[i][k] * U[k][j]
                L[i][j] = (矩阵[i][j] - 和) / U[j][j]
            L[i][i] = 1
            for j in range(i - 1, 列):
                和 = 0
                for k in range(i - 1):
                    和 += L[i][k] * U[k][j]
                U[i][j] = 矩阵[i][j] - 和
        return L, U


if __name__ == "__main__":
    matrix = numpy.array([[2, -2, 1],
                          [0, 1, 2],
                          [5, 3, 1]])
    L, U = LU分解(matrix)
    print(L)
    print(U)
