from random import random
from typing import Tuple


class Node:
    """
    Treap's node
    Treap is a binary tree by key and heap by priority
    """
    def __init__(self, key: int):
        self.key = key
        self.prior = random()   # 优先级
        self.l = None
        self.r = None

def split(root: Node, key: int) -> Tuple[Node, Node]:
    """
        We split current tree into 2 trees with key:

        Left tree contains all keys less than split key.
        Right tree contains all keys greater or equal, than split key
    """
    if root is None:  # None tree is split into 2 Nones
        return (None, None)
    else:
        if key < root.key:
            """
            Right tree's root will be current node.
            Now we split(with the same key) current node's left son
            Left tree: left part of that split
            Right tree's left son: right part of that split
            """
            l, root.l = split(root.l, key)
            return (l, root)
        else:
            """
            Just symmetric to previous case
            """
            root.r, r = split(root.r, key)
            return (root, r)


def merge(left: Node, right: Node) -> Node:
    """
    We merge 2 trees into one.
    Note: all left tree's keys must be less than all right tree's
    """
    if (not left) or (not right):   #如果至少有一个是 None , 返回另一个
        return left or right
    elif left.prior < right.prior:
        # print("left") # @Haor: 没有用到?
        left.r = merge(left.r, right)
        return left
    else:   #以右为头结点, 将左树与右的左孩子重做结合
        """
            Right will be root because it has more priority
            Now we need to merge left tree and right's left son
        """
        right.l = merge(left, right.l)
        return right

def insert(root: Node, key: int) -> Node:
    """
    Insert element

    Split current tree with a key into l, r,
    Insert new node into the middle
    Merge l, node, r into root
    """
    node = Node(key)
    l, r = split(root, key)
    return merge(merge(l, node), r)

def erase(root: Node, key: int) -> Node:
    """
    Erase element

    Split all nodes with keys less into l,
    Split all nodes with keys greater into r.
    Merge l, r
    """
    l, r = split(root, key)
    _, r = split(r, key + 1)
    return merge(l, r)

def pre_print(root: Node):
    """
    前序
    Just recursive print of a tree
    """
    if not root:    # None
        return
    else:
        pre_print(root.l)
        print(root.key, end=" ")
        pre_print(root.r)
def mid_print(root: Node):
    """
    中序
    """
    if not root:
        return
    else:
        print(root.key, end=" ")
        mid_print(root.l)
        mid_print(root.r)

def interactTreap():
    """
    Commands:
    + key to add key into treap
    - key to erase all nodes with key

    After each command, program prints treap
    """
    root = None
    print("本程序将给出一个数字列表, 数字前的'+'代表添加, '-'代表删除. 输入'q'以退出")
    cmd = input()
    while cmd != 'q':
        if cmd[0] == "+":
            root = insert(root, int(cmd[1:]))
        elif cmd[0] == "-":
            root = erase(root, int(cmd[1:]))
        else:
            print("Unknown command")
        mid_print(root)
        cmd = input()

def autoTreap():
    root = None
    print("程序示例:")
    cmds = ["+1", "+3", "+5", "+17", "+19", "+2", "+16", "+4", "+0", "+4", "+4", "+4", "-0", "-3", "-4", "-5", "-10", "+0", ]
    for cmd in cmds:
        print("\n>>>", cmd )
        if cmd[0] == "+":
            root = insert(root, int(cmd[1:]))
        elif cmd[0] == "-":
            root = erase(root, int(cmd[1:]))
        mid_print(root)
    print("\n")
    pre_print(root)

if __name__ == "__main__":
    autoTreap()
    interactTreap()
