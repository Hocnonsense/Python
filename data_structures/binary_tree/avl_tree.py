# -*- coding: utf-8 -*-
'''
An auto-balanced binary tree!
'''
import math, random

class my_queue:
    def __init__(self):
        self.data = list()
        self.head = 0
        self.tail = 0

    def count(self):
        return self.tail - self.head

    def print(self):
        print(self.data)
        print("**************")
        print(self.data[self.head:self.tail])

    def push(self,data):
        """
            在队尾添加一个 data
        """
        self.data.append(data)
        self.tail = self.tail + 1

    def pop(self):
        """
            返回队首 data , 队首后移一位
        """
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    def isEmpty(self):
        return self.head == self.tail

class my_node:
    """
        二叉树的节点: 自身(包括数据, 左孩子, 右孩子, 高度
    """
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getheight(self):
        return self.height

    def setdata(self,data):
        self.data = data

    def setleft(self,node):
        self.left = node

    def setright(self,node):
        self.right = node

    def setheight(self,height):
        self.height = height

class AVLtree:
    def __init__(self):
        self.root = None
        
    def del_node(self,data):
        print("去除: "+str(data))
        if self.root is None:
            print("树空了!")
            return
        self.root = del_node(self.root,data)
    
    def test(self):
        getheight(None)
        print("****")
        self.getheight()

    def getheight(self):
        # print("yyy")
        return getheight(self.root)

    def traversale(self): 
        """
            a level traversale, gives a more intuitive look on the tree
            水平遍历扫描, 更直观的观察二叉树
        """
        q = my_queue()
        q.push(self.root)
        layer = self.getheight()
        if layer == 0:
            return
        else:
            cnt = 1
            while not q.isEmpty():
                node = q.pop()
                space = " "*int(math.pow(2,layer-1))    # 预留给左孩子
                print(space,end = "")
                if node is None:
                    print("*",end = "") # 表示此位置上啥都冇得
                    q.push(None)    # 左孩子空, 右孩子空
                    q.push(None)
                else:
                    print(node.getdata(),end = "")
                    q.push(node.getleft())
                    q.push(node.getright())
                print(space,end = "")
                cnt = cnt + 1   # 下一个节点的位置
                if math.log2(cnt) == int(math.log2(cnt)):   # 如果是2的对数, 说明位于下一行
                    layer = layer - 1 
                    if layer == 0:
                        break
                    else:
                        print() # 换行
            print()
            print("*************************************")
            return

    def insert(self,data):
        print("插入: "+str(data))
        self.root = insert_node(self.root, data)

def getheight(node):
    if node is None:
        return 0
    else:
        return node.getheight()

def recheck_hight(node):
    left, right = getheight(node.getright()), getheight(node.getleft())
    if left > right:
        height =  left + 1
    else:
        height = right + 1
    node.setheight(height)
#
def leftrotation(node):
    r'''
        如图:
          +----A-+        +--B---+
          |      |        |      |
       +--B-+    C     +--Bl   +-A-+
       |    |      --> |       |   |
    +--Bl   Br         UB      Br  C
    | 
    UB
    UB = unbalanced node  
    '''
    print("左旋: ",node.getdata())
    ret = node.getleft()    # B
    node.setleft(ret.getright())    # A.left: B -> Br
    ret.setright(node)  # B.right: Br -> A
    recheck_hight(node)
    recheck_hight(ret)
    return ret

def rightrotation(node):
    '''
        左旋的逆过程
    '''
    print("右旋: ",node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    recheck_hight(node)
    recheck_hight(ret)
    return ret

def rlrotation(node):
    r'''
        如图:
       +-------A-+           +-----A-+          +-Br----+
       |         |           |       |          |       |
    +--B-+       C         +-Br-+    C       +--B    +--A-+
    |    |         -RR->   |    |      -LR-> |       |    |
    Bl   Br-+            +-B    UB           Bl      UB   C
            |            |
            UB           Bl
    RR = rightrotation   LR = leftrotation
    '''
    print("先", end= "")
    node.setleft(rightrotation(node.getleft()))
    print("后", end= "")
    return leftrotation(node)

def lrrotation(node):
    print("先", end= "")
    node.setright(leftrotation(node.getright()))
    print("后", end= "")
    return rightrotation(node)

def insert_node(node, data):
    if node is None:    # 空则插入此数据并返回
        return my_node(data)
    elif data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))  # 在左边添加新节点
        if getheight(node.getleft()) - getheight(node.getright()) == 2: # 发现不平衡
            if data < node.getleft().getdata(): 
                # assert getheight(node.getleft().getleft()) > getheight(node.getleft().getright())
                node = leftrotation(node)   # 新节点是原左孩子的左孩子
            else:
                # assert getheight(node.getleft().getleft()) < getheight(node.getleft().getright())
                node = rlrotation(node)     # 新节点是左孩子的右孩子
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                # assert getheight(node.getright().getright()) < getheight(node.getright().getleft())
                node = lrrotation(node)
            else:
                # assert getheight(node.getright().getright()) > getheight(node.getright().getleft())
                node = rightrotation(node)
    recheck_hight(node)
    return node

def getRightMost(root):
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()

def getLeftMost(root):
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()

def del_node(root,data):
    if root.getdata() == data:  # 本节点即为所求
        if root.getleft() is not None and root.getright() is not None:  # 该节点的两个子节点都非空
            temp_data = getLeftMost(root.getright())    # 取出右孩子最左 (小) 的节点
            root.setdata(temp_data) # 设为该节点的 data
            root.setright(del_node(root.getright(),temp_data))  # 删除移动前的 data
        elif root.getleft() is not None:    # 没有右孩子
            root = root.getleft()   # 直接把左孩子提到自己的位置
        else:   # 没有左孩子
            root = root.getright()  # 直接把右孩子提到自己的位置
    elif root.getdata() > data: # data 比本节点大
        if root.getleft() is None:  # 没有比自己大的节点
            print("无此数据:", data)
            return root
        else:   # 有比自己大的节点
            root.setleft(del_node(root.getleft(), data))    # 过去删除并更新自己
    elif root.getdata() < data: # data 比本节点小
        if root.getright() is None: # 没有比自己小的节点
            print("无此数据:", data)
            return root
        else:   # 有比自己小的节点
            root.setright(del_node(root.getright(), data))  #过去删除并更新自己

    if root is None:
        return root
    else:
        if getheight(root.getleft()) - getheight(root.getright()) == 2:
            if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
                root = leftrotation(root)
            else:
                root = rlrotation(root)
        elif getheight(root.getright()) - getheight(root.getleft()) == 2: # 发现不平衡, 右边过高
            if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
                root = rightrotation(root)
            else:
                root = lrrotation(root)
        recheck_hight(root)
        return root

def avl_tree():
    t = AVLtree()
    t.traversale()
    l = list(range(10))
    l = [#1, 2, 3, 4, ]  # 5, 2, 7, 1, 3, 6, 8, 4, 9] # 2, 0, 7, 6, 9, 3, 5, 1, 4, 8]  # random.shuffle(l) #
                                                            33,                              
                                        20,                                     46,          
                            12,                     28,                 41,             51,  
                    7,              17,         25,     31,         38,     44,     49,  53, 
                4,      10,     15,  19,    23,  27, 30, 32,    36,  40, 43, 45, 48, 50, 52, 
            2,    6,  9, 11, 13, 16, 18, 22, 24, 26, 29,     35, 37, 39, 42,     47, 
          1,  3,  5,  8,     14,         21,                 34, 
          0, ]
    for i in l:
        t.insert(i)
        t.traversale()
    random.shuffle(l)
    #l = [1, ]   # 9, 1]
    for i in l:
        t.del_node(i)
        t.traversale()
平衡二叉搜索树 = avl_tree

if __name__ == "__main__":
    avl_tree()