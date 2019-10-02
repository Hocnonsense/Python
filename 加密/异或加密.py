"""
    author: Christian Bender
    date: 21.12.2017
    class: XORCipher

    This class implements the XOR-cipher algorithm and provides
    some useful methods for encrypting and decrypting strings and
    files.

    Overview about methods

    - 加密 : str
    - 解密 : str
    - 文件加密 : boolean
    - 文件解密 : boolean
"""
class XORCipher(object):

    def __init__(self, 密钥 = 0):
        """
            simple constructor that receives a 密钥 or uses
            default 密钥 = 0
        """
        self.__密钥 = 密钥

    def 加密(self, 信息, 密钥 = 0):
        """
            input: '信息' of type string and '密钥' of type int
            output: encrypted string '信息' as a list of chars
            if 密钥 not passed the method uses the 密钥 by the constructor.
            otherwise 密钥 = 1
        """
        # precondition
        if not (isinstance(密钥, int) and isinstance(信息, (str, list))):
            raise Exception("信息应为字符串类型, 且密钥应为整数类型")
        else:
            密钥 = 密钥 % 255 or self.__密钥 or 1   # 排除异常情况
            译文 = ""
            for 字符 in 信息:
                译文 += chr(ord(字符) ^ 密钥)
            return 译文

    def 解密(self, 信息, 密钥 = 0):
        """
            input: '信息' of type list and '密钥' of type int
            output: decrypted string '信息' as a list of chars
            if 密钥 not passed the method uses the 密钥 by the constructor.
            otherwise 密钥 = 1
        """
        # precondition
        if not (isinstance(密钥, int) and isinstance(信息, (str, list))):
            raise Exception("信息应为字符串类型, 且密钥应为整数类型")
        else:
            密钥 = 密钥 % 255 or self.__密钥 or 1   # 排除异常情况
            译文 = ""
            for 字符 in 信息:
                译文 += chr(ord(字符) ^ 密钥)
            return 译文

    def 文件加密(self, 文件名, 密钥 = 0):
        """
            input: filename (str) and a 密钥 (int)
            output: returns true if 加密 process was
            successful otherwise false
            if 密钥 not passed the method uses the 密钥 by the constructor.
            otherwise 密钥 = 1
        """
        #precondition
        if not (isinstance(密钥, int) and isinstance(文件名, str)):
            raise Exception("信息应为字符串类型, 且密钥应为整数类型")
        else:
            try:
                with open(文件名,"r") as 输入文件, open("加密.out","w+") as 输出文件:
                    # actual 加密-process
                    for 行 in 输入文件:
                        输出文件.write(self.加密(行,密钥))
            except:
                return False
            return True


    def 文件解密(self,文件名, 密钥 = 0):
        """
            input: filename (str) and a 密钥 (int)
            output: returns true if 解密 process was
            successful otherwise false
            if 密钥 not passed the method uses the 密钥 by the constructor.
            otherwise 密钥 = 1
        """
        #precondition
        if not (isinstance(密钥, int) and isinstance(文件名, str)):
            raise Exception("信息应为字符串类型, 且密钥应为整数类型")
        else:
            try:
                with open(文件名,"r") as 输入文件:
                    with open("解密.out","w+") as 输出文件:

                        # actual 加密-process
                        for 行 in 输入文件:
                            输出文件.write(self.解密(行,密钥))

            except:
                return False

            return True

def 异或加密():
    crypt, 密钥 = XORCipher(), 67
    print(crypt.加密("hallo welt",密钥))
    print(crypt.解密(crypt.加密("hallo welt",密钥), 密钥))
    
    if (crypt.文件加密("Prehistoric Men.txt",密钥)):
        print("加密成功! ")
    else:
        print("加密失败. ")
    
    if (crypt.文件解密("加密.out",密钥)):
        print("解密成功! ")
    else:
        print("解密失败. ")
xor_cipher = 异或加密

if __name__ == '__main__':
    异或加密()
