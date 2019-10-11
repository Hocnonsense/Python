'''
二叉搜索树
'''
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent    # 使删除更容易

    def getdata(self):
        return self.data

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getparent(self):
        return self.parent

    def setdata(self, data):
        self.data = data

    def setleft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setparent(self, parent):
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        """
            返回列表中所有节点的字符串。
            按顺序遍历
        """
        nodelist = self.__InOrderTraversal(self.root)
        str = " ".join([repr(i.getdata()) for i in nodelist])
        return str

    def __InOrderTraversal(self, node):
        nodeList = list()
        if node is not None:
            nodeList.insert(0, node)    # 先根遍历
            nodeList = nodeList + self.__InOrderTraversal(node.getleft()) + self.__InOrderTraversal(node.getright())
        return nodeList

    def __isRightChildren(self, node):
        if(node == node.getparent().getright()):
            return True
        else:
            return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):    # 重设孩子的父指针
            newChildren.setparent(node.getparent())
        if(node.getparent() is not None):   # 重设父节点的孩子指针
            if(self.__isRightChildren(node)):
                node.getparent().setRight(newChildren)
            else:
                node.getparent().setleft(newChildren)
        else:
            self.root = newChildren

    def empty(self):
        if self.root is None:
            return True
        else:
            return False

    def insert(self, data):
        new_node = Node(data, None) # 新建点
        if self.empty():    # 若树为空
            self.root = new_node    # 则作为根节点
        else:   # 否则树非空
            parent_node = self.root # 从根节点开始
            while True: # 找到叶子节点
                if data < parent_node.getdata():
                    if parent_node.getleft() == None:
                        parent_node.setleft(new_node)
                        break
                    else:
                        parent_node = parent_node.getleft()
                else:
                    if parent_node.getright() == None:
                        parent_node.setRight(new_node)
                        break
                    else:
                        parent_node = parent_node.getright()
            new_node.setparent(parent_node)

    def getNode(self, data):
        if self.empty():
            raise IndexError("Warning: 树是空的! 请使用非空的二叉树. ")
        else:
            node = self.getRoot()
            while node is not None and node.getdata() is not data:    # 使用惰性求值来避免NoneType属性错误
                if data < node.getdata():
                    node = node.getleft()
                else:
                    node = node.getright()
            return node

    def getRoot(self):
        return self.root

    def getMax(self, node = None):
        if(node is None):
            node = self.getRoot()
        if(not self.empty()):
            while(node.getright() is not None):
                node = node.getright()
        return node

    def getMin(self, node = None):
        if(node is None):
            node = self.getRoot()
        if(not self.empty()):
            node = self.getRoot()
            while(node.getleft() is not None):
                node = node.getleft()
        return node

    def delete(self, data):
        node = self.getNode(data)
        if(node is not None):
            if(node.getleft() is None and node.getright() is None):
                self.__reassignNodes(node, None)
                node = None
            elif(node.getleft() is None):
                self.__reassignNodes(node, node.getright())
            elif(node.getright() is None):
                self.__reassignNodes(node, node.getleft())
            else:
                tmpNode = self.getMax(node.getleft())# 获得左子树的最大叶子节点
                self.delete(tmpNode.getdata())
                node.setdata(tmpNode.getdata()) #并将其作为该节点的新值

    def traversalTree(self, traversalFunction = None, root = None):
        """
            遍历此树, 默认使用类自带的先根遍历方法
        """
        if(traversalFunction is None):
            return self.__InOrderTraversal(self.root)
        else:   # 如果需要用其他函数...
            return traversalFunction(self.root)

def postOrder(curr_node):
    """
        后根遍历
    """
    nodeList = list()
    if curr_node is not None:
        nodeList = postOrder(curr_node.getleft()) + postOrder(curr_node.getright()) + [curr_node]
    return nodeList

def binary_search_tree():
    r'''
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    '''
    t = BinarySearchTree()
    testlist = [8, 3, 6, 1, 10, 14, 13, 4, 7]
    for i in testlist:
        t.insert(i)

    print(t)
    nodelist = t.traversalTree(postOrder, t.root)
    print(" ".join([repr(i.getdata()) for i in nodelist]))
    
    if(t.getNode(6) is not None):
        print("The data 6 exists")
    else:
        print("The data 6 doesn't exist")

    if(t.getNode(-1) is not None):
        print("The data -1 exists")
    else:
        print("The data -1 doesn't exist")

    if(not t.empty()):
        print(("Max Value: ", t.getMax().getdata()))
        print(("Min Value: ", t.getMin().getdata()))

    for i in testlist:
        t.delete(i)
        print(t)

    t.getNode(6)
二叉搜索树 = binary_search_tree

if __name__ == "__main__":
    binary_search_tree()
