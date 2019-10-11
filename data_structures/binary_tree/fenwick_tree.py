"""
Fenwick树，俗称树状数组

也就是二叉索引树(Binary Indexed Tree,BIT)

对于两个数组下标x，y(x < y)，如果x + 2^k = y (k等于x的二进制表示中末尾0的个数)，那么定义(y, x)为一组树上的父子关系，其中y为父结点，x为子结点。
其实Ci还有一种更加普适的定义，它表示的其实是一段原数组A的连续区间和。

a: 给定 n个范围在[0, SIZE]的数字序列a[i](1 <= i < = n)和一个值r (2r+1 <= n)，对于所有的a[k] (r+1 <= k <= n-r)，将它变成 a[k-r ... k+r] 中的中位数。
d: 用一个辅助数组 d[256], 插入 a[i] 执行的是 d[a[i]]++, 删除 a[i] 执行的是 d[a[i]]--； 询问操作是对d数组进行顺序统计, 顺序枚举 i, 找到第一个满足 sum{d[j] | 1 <= j <= i} >= r+1 的 i 就是所求中位数
c: 我们定义 Ci 的值为它的所有子结点的值和 Ai 的总和, 之前提到当 i为奇数时 Ci 一定为叶子结点，所以有 Ci = Ai  (i为奇数), Ci = sum{ A[j]|i - 2^k + 1 <= j <= i } （帮助理解：将j的两个端点相减+1 等于2^k）

至此，树状数组的基础内容就到此结束了，三个函数就诠释了树状数组的所有内容，并且都只需要一行代码实现，单次操作的时间复杂度为 O(log(n))，空间复杂度为 O(n)，所以它是一种性价比非常高的轻量级数据结构。
树状数组解决的基本问题是 单点更新，成端求和。上文中的sum(x)求的是[1, x]的和，如果需要求[x, y]的和，只需要求两次sum函数，然后相减得到，即sum(y) - sum(x-1)。
http://www.cppblog.com/menjitianya/archive/2015/11/02/212171.html
"""

class FenwickTree:
    """
        N   0   1   2   3   4   5   6   7   8
        d   _   a   b   c   d   e   f   g   h
        c0  _   a  ab   c abcd  e  ef   g abcdefgh
        c   _   1   2  23   4  45  46  467  8
    """
    def __init__(self, SIZE): # create fenwick tree with size SIZE
        self.Size = SIZE    # 数据中的最大值
        self.ft = [0 for i in range (0,SIZE)]   # 数组

    def __lowerbit(self, i):
        """
            统计末尾0的个数
            >>> for i in range(9):
            ...     (i, FenwickTree._FenwickTree__lowerbit(None, i))
            ...
            (0, 0)
            (1, 1)
            (2, 2)
            (3, 1)
            (4, 4)
            (5, 1)
            (6, 2)
            (7, 1)
            (8, 8)
        """
        return i & -i

    def update(self, i, val): # update data (adding) in index i in O(lg N)
        while (i < self.Size):
            self.ft[i] += val
            i += self.__lowerbit(i)

    #sum = query
    def query(self, i): # query cumulative data from index 0 to i in O(lg N)
        ret = 0
        while (i > 0):
            ret += self.ft[i]
            i -= self.__lowerbit(i)
        return ret

def fenwick_tree():
    f = FenwickTree(100)
    f.update(1,20)
    f.update(4,4)
    print(f.query(1))
    print(f.query(3))
    print(f.query(4))
    f.update(2,-5)
    print(f.query(1))
    print(f.query(3))
树状数组 = fenwick_tree

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    fenwick_tree()

