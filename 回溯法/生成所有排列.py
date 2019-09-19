'''
    确定给定序列所有可能的排列方式
    使用回溯法
    时间复杂度: O(n! * n),
    n即给定序列的长度
'''


def 生成所有排列(序列 = None):
    try:
        已用元素 = [False for i in range(len(序列))]
    except Exception as e:
        print("输入你要排列的元素")
        序列 = list(map(str, input().split()))
        已用元素 = [False for i in range(len(序列))]
    结果 = list()
    __遍历状态树(序列, 已用元素, 结果)    # , 0
    return 结果
    


def __遍历状态树(序列, 已用元素, 结果, 当前排列 = list()):  # , 已用元素数
    '''
        创建一个状态空间树, 使用 DFS(深度优先) 遍历分支. 
        每个状态都有确定的序列和已用元素
        剩余已用元素的个数决定何时到达序列末尾. 
        如果使用 已用元素数 变量, 可以加快运行速度
    '''

    if [True for i in range(len(序列))] == 已用元素:  # 此处两者不是一个数组, 所以不能用 is 判断
    #if 已用元素数 == len(序列): 
        结果.append(当前排列)  #使其作为一个列表加入新列表
    else:
        for i in range(len(序列)):
            if not 已用元素[i]:
                已用元素[i] = True
                __遍历状态树(序列, 已用元素, 结果, 当前排列 + [i])   # , 已用元素数 + 1
                已用元素[i] = False

def 输出结果(结果):
    for i in 结果:
        print(*i)   # 输出 list 中的内容而非 list 本身
    print()

if __name__ == '__main__':
    序列 = [3, 1, 2, 4]
    输出结果(生成所有排列(序列))
    
    序列 = ["A", "B", "C"]
    输出结果(生成所有排列(序列))

    输出结果(生成所有排列())

