"""
python/black : true
flake8 : passed

规则:
    
1) 每个结点要么是红的, 要么是黑的
2) 根结点是黑的
3) 每个叶结点都是空结点 (NIL),且都是黑的
4) 如果一个结点是红的, 那么它的俩个儿子都是黑的
5) 对每个结点, 从该结点到其子孙结点的所有路径上包含相同数目的黑结点
"""
global check
check = False

class RedBlackTree:
    """
        红黑树，是一种自平衡的BST(binary search tree, 二叉搜索树)。
        此树具有与AVL树相似的性能，但平衡不那么严格，因此在平均情况下，它将执行更快的写入/删除节点和较慢的读取，但由于它们都是平衡的二叉搜索树，两者将获得相同的渐近性能。
        详询 https://en.wikipedia.org/wiki/Red–black_tree
        除非另有指定，否则所有渐近运行时都是根据树的大小指定的。
    """
    def __init__(self, label=None, color=0, parent=None, left=None, right=None):
        """
            label: 值
            color: 0:黑, 1:红
            parent: 父节点
            left: 左孩子
            right: 右孩子
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    # Here are functions which are general to all binary search trees
    def __bool__(self):
        return True

    def __contains__(self, label):
        """
            在树中搜索 label, 若存在返回 True
            O(log(n))
        """
        return self.search(label) is not None

    def __repr__(self):
        from pprint import pformat

        if self.left is None and self.right is None:
            return "'%s %s'" % (self.label, (self.color and "red") or "blk")
        return pformat(
            {
                "%s %s"
                % (self.label, (self.color and "red") or "blk"): (self.left, self.right)
            },
            indent=1,
        )

    def __eq__(self, other):
        """
            两棵树是否等价
        """
        return self.label == other.label and self.left == other.left and self.right == other.right

    def __len__(self):
        """ 返回节点个数"""
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    @property
    def grandparent(self):
        """
            获取祖节点, 否则返回空
        """
        if self.parent is None:
            return None
        else:
            return self.parent.parent
    @property
    def sibling(self):
        """ 获取当前节点的同级节点，如果不存在，则为None。"""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    # Here are functions which are specific to red-black trees
    def __insertrepair(self):
        """
            使新插入的节点保持红黑树结构
        """
        if check: print("__insertrepair", self)
        if self.parent is None:
            self.color = 0  # 根是黑的  (1)
        elif color(self.parent) == 0:
            self.color = 1  # 父节点是黑的, 就变红 (保持黑节点数不变)    (5)
        else:   # 否则父节点是红的 (再添加的必定是单独的黑节点, 必定需要调整)  (5)
            uncle = self.parent.sibling # 找到伯节点 (父节点的兄弟)
            if color(uncle) == 0:   # 伯节点黑色, 为叶子节点或祖节点是红的
                if self.is_left() and self.parent.is_right():   # @Haor: 似乎未使用
                    """
                       +-grnadparent(r)-+                 +-grandparent(r)-+
                       |           *(b) |                ***          *(b) |
                    uncle(b)       +-parent(r)-+     ==>               +-self(r)-+      ==>
                    *None(b)       |           |                       |         |
                                 self(r)     None(b)                 None(b)  parent(r)

                        repair
                    """
                    self.parent.rotate_right()
                    self.__insertrepair()
                elif self.is_right() and self.parent.is_left():
                    if check: print("__insertrepair else-if-elif", self)
                    self.parent.rotate_left()
                    self.__insertrepair()
                elif self.is_left():    # and self.parent.is_left()
                    """
                                    *                          *
                                    |                          |
                           +-grandparent(b)-+          +-parent(b)-+
                           |                |          |           |
                      +-parent(r)-+       *"(b) ==> self(r) +-grandparent(r)-+ ==> repair
                      |           |                         |                |
                    self(r)     *'(b)                     *'(b)            *"(b)
                    """
                    self.grandparent.rotate_right()
                    self.parent.color = 0
                    self.parent.right.color = 1
                else:   # self.is_right() and self.parent.is_right()
                    self.grandparent.rotate_left()
                    self.parent.color = 0
                    self.parent.left.color = 1
            else:   # 伯节点红色
                self.parent.color = 0   # 颜色变黑
                uncle.color = 0
                self.grandparent.color = 1
                self.grandparent.__insertrepair()   # 修复上级
    def __removerepair(self):
        """修复可能被弄乱的树的颜色"""
        if check:print("__removerepair", self)
        if color(self.sibling) == 1:    # 兄弟节点红色, 则变成自己的父节点
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                """
                 *                                  *
                 |                                  |
           +-parent(b)-+                      +-sibling(b)-+
           |           |                      |            |
        self(b)  +-sibling(r)-+     ==>    +-parent(r)-+ right(b)
                 |            |            |           |
              left(b)      right(b)     self(b)      left(b)
                """
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        # assert color(self.sibling) == 0
        if (
                color(self.sibling.left)    == 0
            and color(self.sibling.right)   == 0
        ):  # 下一步离开本函数, 可以直接删除了
            if color(self.parent):  # 黑节点数不变
                """
                     *                         *
                     |                         |
               +-parent(r)-+             +-parent(b)-+
               |           |             |           |
            self(b)    sibling(b) ==> self(b)    sibling(r)
                                         ↖直接删除即可
                """
                self.sibling.color = 1
                self.parent.color = 0
            else:
                """
                     *                         *                               *
                     |                         |                               |
               +-parent(b)-+             +-parent(b)-+                   +-sibling(b)
               |           |             |           |      ...          |
            self(b)    sibling(b) ==> self(b)    sibling(r) ==>    +-parent(r)
                                                                   |
                                                                self(b)
                                                                   ↖直接删除即可
                """
                if check:print("__removerepair if if-else", self)
                self.sibling.color = 1
                if self.parent.sibling:
                    self.parent.__removerepair()    # 黑节点数减一, 父节点需调整
                else:
                    return
        else:
            if self.is_left():
                if color(self.sibling.left) == 1 and color(self.sibling.right) == 0:
                    """
                *                             *
                |                             |
           +-parent----+                 +-parent--+
           |           |                 |         |
        self(b) +-sibling(b)-+    ==> self(b) +-left(b)-+
                |            |                |         |
           +-left(r)-+   right(b)           *'(b) +-sibling(r)-+
           |         |                            |            |
         *'(b)     *"(b)                        *"(b)      right(b)
                    """
                    self.sibling.rotate_right()
                    self.sibling.color = 0
                    self.sibling.right.color = 1
                # assert color(self.sibling.right)   == 1
                """
                *                                     *
                |                                     |
           +-parent(x)-+                        +-sibling(x)-+
           |           |                        |            |
        self(b)  +-sibling(b)-+      ==>    +-parent(b)-+ right(b)
                 |            |             |           |
                 *      +-right(r)-+     self(b)        *
                """
                self.parent.rotate_left()
                self.grandparent.color = self.parent.color
                self.parent.color = 0
                self.parent.sibling.color = 0
            elif self.is_right():
                if color(self.sibling.left) == 0 and color(self.sibling.right) == 1:
                    self.sibling.rotate_left()
                    self.sibling.color = 0
                    self.sibling.left.color = 1
                # assert color(self.sibling.left)   == 1
                self.parent.rotate_right()
                self.grandparent.color = self.parent.color
                self.parent.color = 0
                self.parent.sibling.color = 0

    def rotate_left(self):
        """
            右旋
            向左旋转以此节点为根的子树，并返回新子树的根
            O(1).
              parent                parent
                 |                     |
             +-self-+              +-self-+
             a      |              |      |
               +-rotate-+ ==> +-rotate-+  e
               |        |     |        |
               c        e     a        c
            self 与 rotate 交换值
        """
        a, c, rotate, e = self.left, self.right.left, self.right, self.right.right
        rotate.left, self.left, rotate.right, self.right= a, rotate, c, e
        if a:
            a.parent = rotate
        if c:
            c.parent = rotate
        if e:
            e.parent = self
        rotate.label, self.label, = self.label, rotate.label
        rotate.color, self.color, = self.color, rotate.color
        return self
    def rotate_right(self):
        """
            向右旋转以此节点为根的子树
        """
        a, rotate, c, e = self.left.left, self.left, self.left.right, self.right
        self.left, rotate.left, self.right, rotate.right= a, c, rotate, e
        if a:
            a.parent = self
        if c:
            c.parent = rotate
        if e:
            e.parent = rotate
        rotate.label, self.label, = self.label, rotate.label
        rotate.color, self.color, = self.color, rotate.color
        return self

    def insert(self, label):
        """
            将标签插入到以self为根的子树中，执行保持平衡所需的任何旋转，然后将新根返回到此子树(可能是self)。
            O(log(N))
        """
        if self.label is None:  # 空树的情况, 注意 label可能为0
            self.label = label
            return self # @Haor: ready to delete?
        elif self.label == label:
            return self # @Haor: ready to delete?
        elif label < self.label:
            if self.left:
                self.left.insert(label)
            else:   # 添加节点
                self.left = RedBlackTree(label, 1, self)
                self.left.__insertrepair()
        else:
            if self.right:
                self.right.insert(label)
            else:
                self.right = RedBlackTree(label, 1, self)
                self.right.__insertrepair()
        return self.parent or self  # 返回父节点或自身(根节点时)
    def remove(self, label):
        """删除节点"""
        if check:print("remove", label, self)
        if self.label == label: # 本节点即为所求
            if self.left and self.right:    # 平衡一个最多有一个子节点的节点更容易, 所以我们用比它小的最大节点替换这个节点并删除它.(其实找任何一个作新的头结点都行)
                value = self.left.get_max()
                self.label = value
                self.left.remove(value)
            else:   # 仅有一个非空节点或无
                child = self.left or self.right # 直接替换即可
                if self.color:  # 本节点为红, 子节点必为叶子节点, 可以直接删除
                    if self.is_left():  # 找到上一个节点并删除这个节点
                        self.parent.left = None
                    else:
                        self.parent.right = None
                else:   # 本节点为黑
                    if child is None:   # 没有孩子, 删除必定有影响
                        if self.parent is None: # 全树只有自己
                            return RedBlackTree(None)
                        else:   # 有父节点
                            if check:print("remove if-else-else-if-else", label, self)
                            self.__removerepair()   # 修复节点
                            if self.is_left():  # 并删除
                                self.parent.left = None
                            else:
                                self.parent.right = None
                            self.parent = None
                    else:   # 有(且只有一个)孩子节点, 则孩子节点必是红色的, 把孩子节点提到自己的位置
                        self.label = child.label
                        self.left = child.left
                        self.right = child.right
                        if self.left:
                            self.left.parent = self
                        if self.right:
                            self.right.parent = self
        elif self.label > label:
            if self.left:
                self.left.remove(label)
        else:
            if self.right:
                self.right.remove(label)
        return self.parent or self

    def check_coloring(self):
        """
            递归检查红黑树的 (4)
            self.check_color_properties()
        """
        if self.color:
            if color(self.left) or color(self.right):
                return False
        if self.left and not self.left.check_coloring():
            return False
        if self.right and not self.right.check_coloring():
            return False
        return True
    def black_height(self):
        """
            返回从该节点到树叶子的黑色节点数，如果没有这样的值，则返回None(树的颜色不正确)。
        """
        if self is None:    # 到达叶子
            return 1
        else:
            left = RedBlackTree.black_height(self.left)
            right = RedBlackTree.black_height(self.right)
            if left is None or right is None:   # 子树有问题
                return None
            elif left != right:   # 左右子树高不等
                return None
            else:   # 返回子节点的黑色深度，如果此节点为黑色，则加1
                return left + (1 - self.color)
    def check_color_properties(self):
        """
            检查是否符合规定:
                1) 每个结点要么是红的, 要么是黑的
                2) 根结点是黑的
                3) 每个叶结点都是空结点 (NIL),且都是黑的
                4) 如果一个结点是红的, 那么它的俩个儿子都是黑的
                5) 对每个结点, 从该结点到其子孙结点的所有路径上包含相同数目的黑结点
            O(n) time   (检查(4), (5)
        """
        # (1) 是显然的.
        if self.color:  # (2)
            print("Property 2")
            return False
        # (3) 是显然的, 因为叶子节点必是 None
        if not self.check_coloring():   # (4)
            print("Property 4")
            return False
        if self.black_height() is None: # (5)
            print("Property 5")
            return False
        return True # 验证通过

    # Here are functions which are general to all binary search trees
    def search(self, label):
        """
            在树中搜索 label, 若存在返回该节点
            O(log(n)) time.
        """
        if self.label == label:
            return self
        elif label < self.label:
            if self.left:
                return self.left.search(label)
            else:
                return None
        else:
            if self.right:
                return self.right.search(label)
            else:
                return None

    def floor(self, label):
        """
            返回 lable在此树中的下界, 最低为None, 最高为刚好不比 label大的树或树的最小值
            O(log(n))
        """
        if self.label == label:
            return self.label
        elif self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:   # self.label < label
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
            return self.label
    def ceil(self, label):
        """
            返回 lable在此树中的上界, 最高为None, 最低为刚好不比 label小的树或树的最大值
            O(log(n))
        """
        if self.label == label:
            return self.label
        elif self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
            return self.label

    def get_max(self):
        """
            返回最大值
            O(log(n))
        """
        if self.right: # Go as far right as possible
            return self.right.get_max()
        else:
            return self.label
    def get_min(self):
        """
            返回最小值
            O(log(n))
        """
        if self.left:   # Go as far left as possible
            return self.left.get_min()
        else:
            return self.label

    def is_left(self):
        """
            确定是否是左孩子
        """
        return self.parent and self.parent.left is self
    def is_right(self):
        """
            确定是否是右孩子
        """
        return self.parent and self.parent.right is self

    def preorder_traverse(self):
        """
            带有yield 的函数不再是一个普通函数, 而是一个生成器 generator
            只可以读取它一次, 因为用的时候才生成
        """
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()
    def inorder_traverse(self):
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()
    def postorder_traverse(self):
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label
def color(node):
    """
        返回节点颜色 (若节点为空, 则是根节点)   (2)
    """
    if node:
        return node.color
    else:
        return 0

"""
    红黑树功能测试
"""
def print_results(msg: str, passes: bool) -> None:
    print(str(msg), "成功!" if passes else "失败 :(")

def test_rotations():
    """
        左旋/右旋测试
    """
    tree = RedBlackTree(0)  # 测试树
    tree.left = RedBlackTree(-10, parent=tree)
    tree.right = RedBlackTree(10, parent=tree)
    tree.left.left = RedBlackTree(-20, parent=tree.left)
    tree.left.right = RedBlackTree(-5, parent=tree.left)
    tree.right.left = RedBlackTree(5, parent=tree.right)
    tree.right.right = RedBlackTree(20, parent=tree.right)
    left_rot = RedBlackTree(10) # 右旋样树
    left_rot.left = RedBlackTree(0, parent=left_rot)
    left_rot.left.left = RedBlackTree(-10, parent=left_rot.left)
    left_rot.left.right = RedBlackTree(5, parent=left_rot.left)
    left_rot.left.left.left = RedBlackTree(-20, parent=left_rot.left.left)
    left_rot.left.left.right = RedBlackTree(-5, parent=left_rot.left.left)
    left_rot.right = RedBlackTree(20, parent=left_rot)
    right_rot = RedBlackTree(-10)   # 左旋样树
    right_rot.left = RedBlackTree(-20, parent=right_rot)
    right_rot.right = RedBlackTree(0, parent=right_rot)
    right_rot.right.left = RedBlackTree(-5, parent=right_rot.right)
    right_rot.right.right = RedBlackTree(10, parent=right_rot.right)
    right_rot.right.right.left = RedBlackTree(5, parent=right_rot.right.right)
    right_rot.right.right.right = RedBlackTree(20, parent=right_rot.right.right)
    # print(tree)
    tree = tree.rotate_left()
    # print(tree)
    if tree != left_rot:
        return False
    tree = tree.rotate_right()
    tree = tree.rotate_right()
    # print(tree)
    if tree != right_rot:
        return False
    return True
def test_insert():
    """测试树的insert()方法是否正确平衡、上色和插入"""
    tree = RedBlackTree(0)
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    global check
    check = True
    print(tree)
    tree.insert(11)
    check = False
    ans = RedBlackTree(0, 0)
    ans.left = RedBlackTree(-8, 0, ans)
    ans.right = RedBlackTree(8, 1, ans)
    ans.right.left = RedBlackTree(4, 0, ans.right)
    ans.right.right = RedBlackTree(11, 0, ans.right)
    ans.right.right.left = RedBlackTree(10, 1, ans.right.right)
    ans.right.right.right = RedBlackTree(12, 1, ans.right.right)
    return tree == ans
def test_insert_and_search():
    """Tests searching through the tree for values."""
    tree = RedBlackTree(0).insert(8).insert(-8).insert(5).insert(4)
    tree = tree.insert(12).insert(-6).insert(-10).insert(10).insert(11)
    tree = tree.remove(5).remove(-6).remove(-10)
    if not (11 in tree and 12 in tree and -8 in tree and 0 in tree):    # 该在的不在
        return False
    elif 5 in tree or -6 in tree or -10 in tree or 13 in tree:    # 混进了什么奇怪的东西
        return False
    else:
        return True
def test_insert_delete():
    """
        测试树的insert()和delete()方法，验证元素的插入和删除以及树的平衡。
    """
    tree = RedBlackTree(0)
    tree = tree.insert(-12)
    tree = tree.insert(8)
    tree = tree.insert(-8)
    tree = tree.insert(15)
    tree = tree.insert(4)
    tree = tree.insert(12)
    tree = tree.insert(10)
    tree = tree.insert(9)
    tree = tree.insert(11)
    tree = tree.remove(15)
    tree = tree.remove(-12)
    tree = tree.remove(9)
    if not tree.check_color_properties():
        return False
    elif list(tree.inorder_traverse()) != [-8, 0, 4, 8, 10, 11, 12]:
        return False
    else:
        tree = tree.remove(8)
        tree = tree.remove(-8)
        tree = tree.remove(12)
        tree = tree.remove(11)
        global check
        check = True
        tree = tree.remove(0)
        tree = tree.remove(4)
        tree = tree.remove(10)
        check = False
        return True
def test_floor_ceil():
    """
        测试树中的floor和ceil功能.
    """
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    tuples = [(-20, None, -16), (-10, -16, 0), (8, 8, 8), (50, 24, None)]
    for val, floor, ceil in tuples:
        if tree.floor(val) != floor or tree.ceil(val) != ceil:
            return False
    return True
def test_tree_traversal():
    """
        测试三种遍历方式
        及连续插入节点
    """
    tree = RedBlackTree(0)
    tree = tree.insert(-16).insert(16).insert(8).insert(24).insert(20).insert(22)
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    elif list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    elif list(tree.postorder_traverse()) != [-16, 8, 20, 24, 22, 16, 0]:
        return False
    else:
        return True
def test_min_max():
    """Tests the min and max functions in the tree."""
    tree = RedBlackTree(0)
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    return tree.get_max() == 24 and tree.get_min() == -16
def test_insertion_speed():
    """
        大量插入以测试平衡性
        O(log(n))
    """
    tree = RedBlackTree(-1)
    for i in range(300000):
        print("\r插入", str(i), end = "")
        tree = tree.insert(i)
    for i in range(200000, 100000, -1):
        print("\r删除", str(i), end = "")
        tree = tree.remove(i)
    print("\r", end = "")
    return True

def pytests():
    assert test_rotations()
    assert test_insert()
    assert test_insert_and_search()
    assert test_insert_delete()
    assert test_floor_ceil()
    assert test_tree_traversal()
    assert test_tree_chaining()

def main():
    # pytests()
    print_results("左右旋测试", test_rotations())
    print_results("插入测试", test_insert())
    print_results("搜索测试", test_insert_and_search())
    print_results("删除测试", test_insert_delete())
    print_results("上下值测试", test_floor_ceil())
    print_results("遍历测试", test_tree_traversal())
    print_results("最值测试", test_min_max())
    print("检查树的平衡性...\n稍等片刻.")
    test_insertion_speed()
    print("完成!")

if __name__ == "__main__":
    main()