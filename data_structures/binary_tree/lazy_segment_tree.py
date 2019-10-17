"""
在需要对线段树进行区间修改(如给整个区间加减某一值，或全部改为某一值)时，若反复使用之前的单点修改，那么算法的时间复杂度将达到一个恐怖的级别(单次修改nlogn，超出了不用线段树的时间复杂度)，因此要引入“标记”思想。

懒标记 (Lazy Tag), 也有的地方翻译成 "延迟标记" (听起来高端...), 就是指在更新一部分区间的时候, 不更新这个区间里面的每个点, 而是 (懒惰地) 把这个区间分割成很多个能用线段树上的点表示的区间 (当然是分的区间越少越好, 也就是说每个区间越大越好), 只修正代表这个区间的点, 再把这些区间标记下, 下次如果要查询的区间与这个区间有交集并且没有包含这个区间, 就说明需要 "分割" 这个区间, 再将这个区间向下修正. 这样时间复杂度就可以优化很多. 
"""

import math

class SegmentTree:

    def __init__(self, A):
        """
            N:int # len(A)
            st:list # 
            lazy:list # 
            flag:list(bool) # 如果True: 对应st (及其子节点) 的值需要被更新而未被更新
        """
        self.N = len(A)  # 长度
        self.st = [0 for i in range(0,4*self.N)] # approximate the overall size of segment tree with array N
        self.lazy = [0 for i in range(0,4*self.N)] # create array to store lazy __update
        self.flag = [0 for i in range(0,4*self.N)] # flag for lazy __update
        self.__build(1, 1, self.N, A)

    def __left(self, idx):
        return idx*2

    def __right(self, idx):
        return idx*2 + 1

    def __build(self, idx, l, r, A):
        if l==r:
            self.st[idx] = A[l-1]
        else :
            mid = (l+r)//2
            self.__build(self.__left(idx),l,mid, A)
            self.__build(self.__right(idx),mid+1,r, A)
            self.st[idx] = max(self.st[self.__left(idx)] , self.st[self.__right(idx)]) 

    def __lazySet(self, idx, l, r):
        if l!=r:    # 不是叶子节点, 此时不进入else, 而提前终止
            self.lazy[self.__left(idx)] = self.st[idx]   # 暂存对应值, 等待修改
            self.lazy[self.__right(idx)] = self.st[idx]
            self.flag[self.__left(idx)] = True
            self.flag[self.__right(idx)] = True

    def __lazyCheck(self, idx, l, r):
        if self.flag[idx] == True:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.__left(idx)] = self.lazy[idx]
                self.lazy[self.__right(idx)] = self.lazy[idx]
                self.flag[self.__left(idx)] = True
                self.flag[self.__right(idx)] = True

    def __query(self, idx, l, r, a, b): # __query with O(lg N)
        self.__lazyCheck(idx, l, r)
        if b<l or r<a:
            return -math.inf
        if a <= l and r <= b:
            return self.st[idx]
        else:
            mid = (l+r)//2
            q1 = self.__query(self.__left(idx), l, mid, a, b)
            q2 = self.__query(self.__right(idx), mid + 1, r, a, b)
            return max(q1,q2)

    def query(self, a, b):
        """
            self.__query(1, 1, N, a, b) for query max of [a,b]
        """
        return self.__query(1, 1, self.N, a, b)

    def __update(self, idx, l, r, a, b, val): # __update(1, 1, N, a, b, v) for __update val v to [a,b]
        self.__lazyCheck(idx, l, r)
        if b<l or r<a:  # 不在给出的区间中
            pass
        elif a <= l and r <= b:
            self.st[idx] = val
            self.__lazySet(idx, l, r)
        else:
            mid = (l+r)//2
            self.__update(self.__left(idx),l,mid,a,b,val)
            self.__update(self.__right(idx),mid+1,r,a,b,val)
            self.st[idx] = max(self.st[self.__left(idx)] , self.st[self.__right(idx)])

    def update(self, a, b, val):
        self.__update(1, 1, self.N, a, b, val)

    def showData(self):
        showList = list()
        for i in range(1,self.N+1):
            showList += [self.__query(1, 1, self.N, i, i)]
        print(showList)

def lazy_segment_tree():
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = len(A)
    segt = SegmentTree(A)
    print(segt.query(4,6))
    print(segt.query(7,11))
    print(segt.query(7,12))
    segt.update(1,3,111)
    print(segt.query(1,15))
    segt.update(7,8,235)
    segt.showData()
    pass

if __name__ == '__main__':
    lazy_segment_tree()
