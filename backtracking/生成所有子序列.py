'''
    在这里, 我们希望给出输入序列的所有子序列
    使用回溯法
    时间复杂度: O(2^n),
    n还是输入序列的长度.
'''


def 生成所有子序列(序列):
    结果 = list()
    create_state_space_tree(序列, 0)


def create_state_space_tree(序列, 已用元素数, 当前序列 = list()):
    '''
        创建一个状态空间树，使用DFS遍历每个分支。
        我们知道每个状态只有两个孩子(可能)。
        index决定什么时候终止。
    '''
    if 已用元素数 == len(序列):
        print(当前序列)
    else:
        create_state_space_tree(序列, 已用元素数 + 1, 当前序列)    # 不使用当前元素
        当前序列.append(序列[已用元素数])
        create_state_space_tree(序列, 已用元素数 + 1, 当前序列)    # 使用当前元素
        当前序列.pop()


        
def 输出结果(结果):
    for i in 结果:
        print(*i)   # 输出 list 中的内容而非 list 本身

if __name__ == '__main__':


    序列 = [3, 1, 2, 4]
    生成所有子序列(序列)

    序列 = ["A", "B", "C"]
    生成所有子序列(序列)
