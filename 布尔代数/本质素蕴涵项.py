# -*- coding: utf-8 -*-

def 十进制转二进制(二进制位数, 最小项):
    """
    >>> 十进制转二进制(3,[1.5])
    ['0.00.01.5']
    """
    暂存 = list()
    for m in 最小项:
        s = str()
        for i in range(二进制位数):
            s = str(m%2) + s
            m //= 2
            #print(行, s, m)
        暂存.append(s)
    return 暂存

def 组合极小项(字串1, 字串2):
    """
    >>> 组合极小项('0010','0110')
    '0_10'
    
    >>> 组合极小项('0110','1101')
    False
    """
    结果 = list(字串1)
    不同 = 0
    for i in range(len(结果)):
        if 字串1[i] != 字串2[i]:
            不同 += 1
            结果[i] = '_'
    #print("".join(结果), "".join(l2))
    结果 = "".join(结果)
    if 不同 > 1:
        结果 = False
    return(结果)

def 计算素蕴涵项(二进制):
    """
        检查二进制数, 提取所有二进制位下有且仅有一位相同的数字并归为一类

    >>> 计算素蕴涵项(['0.00.01.5'])
    ['0.00.01.5']
    """
    素蕴涵项 = list()
    while 二进制 != list():
        暂存 = list(set(二进制))
        不可组合 = [True]*len(暂存)
        二进制 = list()
        for i in range(len(暂存)):
            for j in range(i+1, len(暂存)):
                极小项 = 组合极小项(暂存[i], 暂存[j])
                #print(i, j, 极小项)
                if 极小项 != False:
                    不可组合[i], 不可组合[j] = False, False
                    二进制.append(极小项)
        for i in range(len(暂存)):
            if 不可组合[i]:
                素蕴涵项.append(暂存[i])
        #print(*不可组合, 二进制, 素蕴涵项)
    return 素蕴涵项

def 对应(字串1, 字串2, 计数):
    """
    >>> 对应('__1','011',2)
    True
    
    >>> 对应('01_','001',1)
    False
    """
    for i in range(len(字串1)):
        if 字串1[i] != 字串2[i]:
            计数 -= 1
    if 计数 == 0:
        return True
    else:
        return False 
        
def 生成素蕴涵项表(素蕴涵项, 二进制):
    """
        生成素蕴涵项行, 二进制列的表
    >>> 生成素蕴涵项表(['0.00.01.5'],['0.00.01.5'])
    [[True]]
    """
    素蕴涵项表 = [[[False] for 列 in range(len(二进制))] for 行 in range(len(素蕴涵项))]
    for 行 in range(len(素蕴涵项)):
        计数 = 素蕴涵项[行].count('_')
        for 列 in range(len(二进制)):
            if(对应(素蕴涵项[行], 二进制[列], 计数)):
                素蕴涵项表[行][列] = True

    return 素蕴涵项表

def 简约(素蕴涵项表, 素蕴涵项):
    """
    >>> 简约([[1]],['0.00.01.5'])
    ['0.00.01.5']
    
    >>> 简约([[1]],['0.00.01.5'])
    ['0.00.01.5']
    """
    选择 = [0]*len(素蕴涵项表)
    for 列 in range(len(素蕴涵项表[0])):  # 找到仅对应一个素蕴涵项的二进制数并标记
        计数, 其余最小项 = 0, -1
        for 行 in range(len(素蕴涵项表)):
            if 素蕴涵项表[行][列] == True:
                计数 += 1
                其余最小项 = 行
        if 计数 == 1:
            选择[其余最小项] = 1
    #print(选择)

    暂存 = list()
    for 行 in range(len(素蕴涵项表)):
        if 选择[行] == 1:
            for 列 in range(len(素蕴涵项表[0])):
                if 素蕴涵项表[行][列] == True:
                    for k in range(len(素蕴涵项表)):
                        素蕴涵项表[k][列] = False
            暂存.append(素蕴涵项[行])
    #print(素蕴涵项表)
    #print(暂存)

    while True:
        最多覆盖, 当前覆盖, 其余最小项 = 0, 0, None
        for 行 in range(len(素蕴涵项表)):
            当前覆盖 = 素蕴涵项表[行].count(True)
            if 当前覆盖 > 最多覆盖:
                最多覆盖 = 当前覆盖
                其余最小项 = 行
        
        if 最多覆盖 == 0:
            return 暂存
        else:
            暂存.append(素蕴涵项[其余最小项])
            
            for 列 in range(len(素蕴涵项表[0])):
                if 素蕴涵项表[其余最小项][列] == True:
                    for k in range(len(素蕴涵项表)):
                        素蕴涵项表[k][列] = False

def 本质素蕴涵项():
    print("输入二进制位数: ", end = "")
    二进制位数 = int(input())
    print("输入整数最小项, 以十进制表示, 以空格分隔: ", end = "")
    最小项 = [int(x) for x in input().split()]
    二进制 = 十进制转二进制(二进制位数, 最小项)
    #print("输入转化为二进制: ", 二进制)

    素蕴涵项 = 计算素蕴涵项(二进制)
    print("素蕴涵项有: ", 素蕴涵项)
    素蕴涵项表 = 生成素蕴涵项表(素蕴涵项, 二进制)
    #print("素蕴涵项表 为", *素蕴涵项表)

    本质素蕴涵项 = 简约(素蕴涵项表,素蕴涵项)
    print("本质素蕴涵项为: ", 本质素蕴涵项)

if __name__ == '__main__':
    from doctest import testmod
    testmod()   # 直接导致无法显示中文字符
    本质素蕴涵项()
