"""
线段树（segment tree），顾名思义， 是用来存放给定区间（segment, or interval）内对应信息的一种数据结构。
与树状数组（binary indexed tree）相似

从数据结构的角度来说，线段树是用一个完全二叉树来存储对应于其每一个区间（segment）的数据。该二叉树的每一个结点中保存着相对应于这一个区间的信息。同时，线段树所使用的这个二叉树是用一个数组保存的，与堆（Heap）的实现方式相同。

1. T的根结点代表整个数组所在的区间对应的信息，及arr[0:N]（不含N)所对应的信息。 
2. T的每一个叶结点存储对应于输入数组的每一个单个元素构成的区间arr[i]所对应的信息，此处0≤i<N。 
3. T的每一个中间结点存储对应于输入数组某一区间arr[i:j]对应的信息，此处0≤i<j<N。
"""

import math

class SegmentTree:

    def __init__(self, A):
        self.N = len(A)
        self.st = [0] * (4 * self.N) # 最小要建 4*N 大小的数组
        self.__build(1, 0, self.N - 1, A)

    def __left(self, idx):
        return idx * 2

    def __right(self, idx):
        return idx * 2 + 1

    def __build(self, idx, l, r, A):
        """
            idx :int # 指针位置, 指向下一个元素插入位置
            l   :int # 区间左界
            r   :int # 区间右界
            A   :list # 创建线段树所需表
        """
        # print(l, r, idx, )
        if l == r:
            self.st[idx] = A[l]
        else:
            mid = (l + r) // 2
            self.__build(self.__left(idx), l, mid, A)
            self.__build(self.__right(idx), mid + 1, r, A)
            self.st[idx] = max(self.st[self.__left(idx)] , self.st[self.__right(idx)])  # st[i]记录原数组对应区间中的最大值

    def __query(self, idx, l, r, a, b): #query(1, 1, N, a, b) for query max of [a,b]
        if b<l or r<a:  # 不在给出的区间中
            return -math.inf    # 不作考虑
        elif a <= l and r <= b: # 所求区间在当前区间内
            return self.st[idx] # 即返回该中间节点值
        else:   # 区间横跨几个不同的中间节点
            mid = (l+r)//2  # 分治法
            q1 = self.__query(self.__left(idx), l, mid, a, b)
            q2 = self.__query(self.__right(idx), mid + 1, r, a, b)
            return max(q1, q2)  # 取最大值

    def query(self, a, b):
        return self.__query(1, 0, self.N - 1, a - 1, b - 1)

    def __update(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if r < a or l > b:
            return True
        elif l == r :
            self.st[idx] = val
            return True
        else:
            mid = (l+r)//2
            self.__update(self.__left(idx), l, mid, a, b, val)
            self.__update(self.__right(idx), mid+1, r, a, b, val)
            self.st[idx] = max(self.st[self.__left(idx)] , self.st[self.__right(idx)])
            return True

    def update(self, a, b, val):
        """
            将区间[a,b]的所有值都变为val
        """
        return self.__update(1, 0, self.N - 1, a - 1, b - 1, val)

    def showData(self):
        showList = list()
        for i in range(1, self.N+1):
            showList += [self.query(i, i)]
        print(showList)

def segment_tree():
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    segt = SegmentTree(A)
    print(segt.query(4, 6))
    print(segt.query(7, 11))
    print(segt.query(7, 12))
    segt.update(1,3,111)
    print(segt.query(1, 15))
    segt.update(7,8,235)
    segt.showData()
    print(segt.st)

if __name__ == '__main__':
    segment_tree()

