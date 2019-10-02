"""
Hill Cipher:
    下面定义的类‘Hill加密’实现Hill密码算法。
    Hill密码用到了现代线性代数。
    在这个算法中，您有一个加密密钥矩阵, 用来加密和解密。

算法:
    假设加密密钥的阶数为N(因为它是方阵)。
    您的文本被分成长度为N的批次，并通过从A=0开始的简单映射转换为数值向量，依此类推。

    然后，将密钥与新创建的批处理向量相乘，以获得编码向量。
    在每个乘法模块36之后，对向量执行计算，以便使数字在0和36之间，然后用它们相应的字母数字进行映射。

    在解密时，找到解密密钥，它是加密密钥模块36的逆。
    重复相同的过程以解密以取回原始消息。
    
限制：
    加密密钥矩阵的行列式必须是相对素的w.r.t36。

注：
    在此代码中实现的算法只考虑文本中的字母数字。
    如果要加密的文本的长度不是Break 密钥的倍数(一批字母的长度)，则将文本的最后一个字符添加到文本中，直到文本的长度达到阶的倍数。
    因此解密后的文本可能与原始文本略有不同。

References:
https://apprendre-en-ligne.net/crypto/hill/Hillciph.pdf
https://www.youtube.com/watch?v=kfmNeskzs2o
https://www.youtube.com/watch?v=4RhLNDqcjpA

"""
import numpy
import 密码数学模块 as 密码数学

class Hill加密:
    字符表 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # This cipher takes alphanumerics into account
    # i.e. a total of 36 characters

    字符编号 = lambda self, 字符: self.字符表.index(字符)
    替换字符 = lambda self, 字符编号: self.字符表[round(字符编号)]

    """
        numpy.vectorize()只是为了方便，效率比较低。
        定义了一个矢量函数，输入是嵌套化的对象序列或者是numpy数组， 
        输出是单个或元组的numpy数组。跟 map（）很类似。将函数pyfunc作用在序列化的对象上。 
    """
    # take x and return x % len(字符表)
    取余 = numpy.vectorize(lambda x: x % 36)  # len(self.字符表)
    取整 = numpy.vectorize(lambda x: round(x))
    
    def __init__(self, 加密密钥):
        """
        加密密钥 is an NxN numpy matrix
        """
        self.加密密钥 = self.取余(加密密钥) # mod 36 calc's on the 加密 密钥
        self.检验行列式() # validate the determinant of the encryption 密钥
        self.解密密钥 = None
        self.阶 = len(加密密钥)  # 加密密钥.shape[0]  # 

    def 检验行列式(self):
        行列式 = round(numpy.linalg.det(self.加密密钥))    #计算任何一个数组a的行列式，但是这里要求数组的最后两个维度必须是方阵
        if 行列式 < 0:
            行列式 = 行列式 % len(self.字符表)
        req_l = len(self.字符表)
        if 密码数学.最小公约数(行列式, req_l) != 1:
            raise ValueError("加密密钥判别式的模({0}) 与字符表长度 {1} 不互素.\n请更换密钥.".format(行列式, req_l))

    def 处理文字(self, 信息):
        信息 = [char for char in 信息.upper() if char in self.字符表]
        加尾 = 信息[-1]
        while len(信息) % self.阶 != 0:
            信息.append(加尾)
        return ''.join(信息)
    
    def 加密(self, 信息):
        信息 = self.处理文字(信息)
        加密信息 = ''

        for i in range(0, len(信息) - self.阶 + 1, self.阶):
            分组 = 信息[i:i+self.阶]
            #分组向量 = list(map(self.字符编号, 分组))
            #print(分组向量)
            分组向量 = numpy.matrix(list(map(self.字符编号, 分组))).T
            加密处理 = self.取余(self.加密密钥.dot(分组向量)).T.tolist()[0]    # dot是矩阵乘法, [0]可以不需要
            加密分组 = ''.join(map(self.替换字符, 加密处理))
            加密信息 += 加密分组
        return 加密信息

    def 计算解密密钥(self):
        行列式 = round(numpy.linalg.det(self.加密密钥))
        if 行列式 < 0:
            行列式 = 行列式 % len(self.字符表)
        矩阵模的模逆 = None
        for i in range(len(self.字符表)):
            if (行列式 * i) % len(self.字符表) == 1:
                矩阵模的模逆 = i
                break
        逆密钥 = 矩阵模的模逆 * numpy.linalg.det(self.加密密钥) * numpy.linalg.inv(self.加密密钥)
        self.解密密钥 =  self.取整(self.取余(逆密钥))
    
    def 解密(self, 信息):
        self.计算解密密钥()
        信息 = self.处理文字(信息)
        解密信息 = ''
        for i in range(0, len(信息) - self.阶 + 1, self.阶):
            分组 = 信息[i:i+self.阶]
            分组向量 = numpy.matrix(list(map(self.字符编号, 分组))).T
            解密处理 = self.取余(self.解密密钥.dot(分组向量)).T.tolist()[0]
            解密分组 = ''.join(list(map(self.替换字符, 解密处理)))
            解密信息 += 解密分组
        return 解密信息

def Hill加密算法():
    阶 = int(input("输入加密密钥的阶: "))
    加密矩阵 = list()

    print("输入加密密钥的每一行, 同一行中的数字用空格分隔")
    for i in range(阶):
        行 = list(map(int, input().split()))
        加密矩阵.append(行)
    hc = Hill加密(numpy.matrix(加密矩阵))

    选项 = input("需要加密还是解密? (1 or 2)\n1. 加密\n2. 解密\n")
    if 选项 == '1':
        信息 = input("输入需要加密的信息: ")
        print("加密后的信息为: ")
        print(hc.加密(信息))
    elif 选项 == '2':
        信息 = input("输入需要解密的信息: ")
        print("解密后的信息为: ")
        print(hc.解密(信息))
hill_cipher = Hill加密算法

if __name__ == "__main__":
    Hill加密算法()
