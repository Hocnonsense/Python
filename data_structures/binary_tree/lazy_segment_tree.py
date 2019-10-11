"""
在需要对线段树进行区间修改(如给整个区间加减某一值，或全部改为某一值)时，若反复使用之前的单点修改，那么算法的时间复杂度将达到一个恐怖的级别(单次修改nlogn，超出了不用线段树的时间复杂度)，因此要引入“标记”思想。
"""

import math

class SegmentTree:

    def __init__(self, A):
        """
            N:int # len(A)
            st:list # 
            lazy:list # 
            flag:list # bool
        """
        self.N = len(A)  # 长度
        self.st = [0 for i in range(0,4*self.N)] # approximate the overall size of segment tree with array N
        self.lazy = [0 for i in range(0,4*self.N)] # create array to store lazy update
        self.flag = [0 for i in range(0,4*self.N)] # flag for lazy update
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
    def __query(self, idx, l, r, a, b): # __query with O(lg N)
        if self.flag[idx] == True:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.__left(idx)] = self.lazy[idx]
                self.lazy[self.__right(idx)] = self.lazy[idx]
                self.flag[self.__left(idx)] = True
                self.flag[self.__right(idx)] = True
        if b<l or r<a:
            return -math.inf
        if a <= l and r <= b:
            return self.st[idx]
        else:
            mid = (l+r)//2
            q1 = self.__query(self.__left(idx),l,mid,a,b)
            q2 = self.__query(self.__right(idx),mid+1,r,a,b)
            return max(q1,q2)

    def query(self, a, b):
        """
            self.__query(1, 1, N, a, b) for query max of [a,b]
        """
        return self.__query(1, 1, self.N, a, b)

    # update with O(lg N) (Normal segment tree without lazy update will take O(Nlg N) for each update)
    def update(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if self.flag[idx] == True:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l!=r:
                self.lazy[self.__left(idx)] = self.lazy[idx]
                self.lazy[self.__right(idx)] = self.lazy[idx]
                self.flag[self.__left(idx)] = True
                self.flag[self.__right(idx)] = True

        if r < a or l > b:
            return True
        if l >= a and r <= b :
            self.st[idx] = val
            if l!=r:
                self.lazy[self.__left(idx)] = val
                self.lazy[self.__right(idx)] = val
                self.flag[self.__left(idx)] = True
                self.flag[self.__right(idx)] = True
            return True
        mid = (l+r)//2
        self.update(self.__left(idx),l,mid,a,b,val)
        self.update(self.__right(idx),mid+1,r,a,b,val)
        self.st[idx] = max(self.st[self.__left(idx)] , self.st[self.__right(idx)])
        return True

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
    segt.update(1,1,N,1,3,111)
    print(segt.query(1,15))
    segt.update(1,1,N,7,8,235)
    segt.showData()
    pass

if __name__ == '__main__':
    lazy_segment_tree()
