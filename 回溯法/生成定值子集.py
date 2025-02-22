'''
    子集合和问题表示一组非负整数，和一个给定值，
    确定给定集合的所有可能子集，它们的和等于给定值。
    所选数字的和必须等于给定的数字M，并且一个数字只能使用一次。
'''


def 生成定值子集(集合: list, 给定值: int):
    结果, 子集 = list(), list()
    当前元素 = 0
    __生成定值子集(集合, 给定值, 当前元素, 子集, 结果)
    return 结果

def __生成定值子集(集合, 给定值, 当前元素, 子集, 结果 = list()):
    '''
        创建一个状态空间树，使用DFS遍历每个分支。
        当下面给出的两个条件之一满足时，它终止节点的分支。
        该算法遵循深度优先搜索，在节点不可分支时回溯。
    '''
    if sum(子集) > 给定值 or (sum(集合[当前元素:]) + sum(子集)) < 给定值:
        return
    elif sum(子集) == 给定值:
        结果.append(子集)
        return
    else:
        for 当前元素 in range(当前元素,len(集合)):
            __生成定值子集(集合, 给定值, 当前元素 + 1, 子集 + [集合[当前元素]], 结果)

'''
remove the comment to take an input from the user 

print("Enter the elements")
集合 = list(map(int, input().split()))
print("Enter 给定值 sum")
给定值 = int(input())

'''
if __name__ == '__main__':
    集合 = [3, 34, 4, 12, 5, 2]
    给定值 = 9
    结果 = 生成定值子集(集合,给定值)
    print(*结果)