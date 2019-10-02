import random

class 一次一秘:
    def 加密(self, text):
        """
            使用伪随机数加密
        """
        明文表 = [ord(明文) for 明文 in text]
        密钥表, 密文表 = list(), list()
        for 明文 in 明文表:
            密钥 = random.randint(1, 300)
            密文 = (明文+密钥)*密钥
            密钥表.append(密钥)
            密文表.append(密文)
        return 密钥表, 密文表

    def 解密(self, 密钥表, 密文表):
        """
            使用伪随机数解密
        """
        明文表 = list()
        for 明文 in range(len(密钥表)):
            p = int((密文表[明文]-(密钥表[明文])**2)/密钥表[明文])
            明文表.append(chr(p))
        明文表 = ''.join([明文 for 明文 in 明文表])
        return 明文表

def 一次一秘加密():
    密钥表, 密文表 = 一次一秘().加密('Hello')
    print(密钥表, 密文表)
    print(一次一秘().解密(密钥表, 密文表))
onepad_cipher = 一次一秘加密

if __name__ == '__main__':
    一次一秘加密()