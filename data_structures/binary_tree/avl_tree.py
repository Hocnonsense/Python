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
        print("delete:"+str(data))
        if self.root is None:
            print("Tree is empty!")
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
        print("insert:"+str(data))
        self.root = insert_node(self.root, data)

def my_max(a,b):
    if a > b:
        return a
    return b

def leftrotation(node):
    r'''
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB
  
    UB = unbalanced node  
    '''
    print("left rotation node:",node.getdata())
    ret = node.getleft()
    node.setleft(ret.getright())
    ret.setright(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rightrotation(node):
    '''
        a mirror symmetry rotation of the leftrotation
    '''
    print("right rotation node:",node.getdata())
    ret = node.getright()
    node.setright(ret.getleft())
    ret.setleft(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    h2 = my_max(getheight(ret.getright()),getheight(ret.getleft())) + 1         
    ret.setheight(h2)
    return ret

def rlrotation(node):
    r'''
            A              A                    Br      
           / \            / \                  /  \
          B   C    RR    Br  C       LR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C  
             \        /
             UB     Bl
    RR = rightrotation   LR = leftrotation
    '''
    node.setleft(rightrotation(node.getleft()))
    return leftrotation(node)

def lrrotation(node):
    node.setright(leftrotation(node.getright()))
    return rightrotation(node)

def getRightMost(root):
    while root.getright() is not None:
        root = root.getright()
    return root.getdata()

def getLeftMost(root):
    while root.getleft() is not None:
        root = root.getleft()
    return root.getdata()

def del_node(root,data):
    if root.getdata() == data:
        if root.getleft() is not None and root.getright() is not None:
            temp_data = getLeftMost(root.getright())
            root.setdata(temp_data)
            root.setright(del_node(root.getright(),temp_data))
        elif root.getleft() is not None:
            root = root.getleft()
        else:
            root = root.getright()
    elif root.getdata() > data:
        if root.getleft() is None:
            print("No such data")
            return root
        else:
            root.setleft(del_node(root.getleft(),data))
    elif root.getdata() < data:
        if root.getright() is None:
            return root
        else:
            root.setright(del_node(root.getright(),data))
    if root is None:
        return root
    if getheight(root.getright()) - getheight(root.getleft()) == 2:
        if getheight(root.getright().getright()) > getheight(root.getright().getleft()):
            root = rightrotation(root)
        else:
            root = lrrotation(root)
    elif getheight(root.getright()) - getheight(root.getleft()) == -2:
        if getheight(root.getleft().getleft()) > getheight(root.getleft().getright()):
            root = leftrotation(root)
        else:
            root = rlrotation(root)
    height = my_max(getheight(root.getright()),getheight(root.getleft())) + 1
    root.setheight(height)
    return root

def getheight(node):
    if node is None:
        return 0
    else:
        return node.getheight()
#
def insert_node(node, data):
    if node is None:
        return my_node(data)
    elif data < node.getdata():
        node.setleft(insert_node(node.getleft(),data))
        if getheight(node.getleft()) - getheight(node.getright()) == 2: #an unbalance detected
            if data < node.getleft().getdata():       #new node is the left child of the left child
                node = leftrotation(node)
            else:
                node = rlrotation(node)             #new node is the right child of the left child
    else:
        node.setright(insert_node(node.getright(),data))
        if getheight(node.getright()) - getheight(node.getleft()) == 2:
            if data < node.getright().getdata():
                node = lrrotation(node)
            else:
                node = rightrotation(node)
    h1 = my_max(getheight(node.getright()),getheight(node.getleft())) + 1
    node.setheight(h1)
    return node

def main():
    t = AVLtree()
    t.traversale()
    l = list(range(10))
    random.shuffle(l)
    for i in l:
        t.insert(i)
        t.traversale()
    input()
        
    random.shuffle(l)
    for i in l:
        t.del_node(i)
        t.traversale()
        
if __name__ == "__main__":
    main()