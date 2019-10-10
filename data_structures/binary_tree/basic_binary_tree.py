class Node: # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display(tree): # 显示树
    if tree is not None: 
        display(tree.left)
        print(tree.data)
        display(tree.right)

def depth_of_tree(tree): # 树的深度.
    if tree is None:
        return 0
    else:
        return max(depth_of_tree(tree.left), depth_of_tree(tree.right)) + 1

def is_full_binary_tree(tree): # This functions returns that is it full binary tree or not?
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        return False

def basic_binary_tree(): # basic_binary_tree func for testing.
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is: ")
    display(tree)
基本二叉树 = basic_binary_tree

if __name__ == '__main__':
    basic_binary_tree()
