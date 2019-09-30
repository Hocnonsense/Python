LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def 解码(信息, 密钥表 = len(LETTERS)):
    """
    >>> 解码('TMDETUX PMDVU')
    密钥 #0 解密结果: TMDETUX PMDVU
    密钥 #1 解密结果: SLCDSTW OLCUT
    密钥 #2 解密结果: RKBCRSV NKBTS
    密钥 #3 解密结果: QJABQRU MJASR
    密钥 #4 解密结果: PIZAPQT LIZRQ
    密钥 #5 解密结果: OHYZOPS KHYQP
    密钥 #6 解密结果: NGXYNOR JGXPO
    密钥 #7 解密结果: MFWXMNQ IFWON
    密钥 #8 解密结果: LEVWLMP HEVNM
    密钥 #9 解密结果: KDUVKLO GDUML
    密钥 #10 解密结果: JCTUJKN FCTLK
    密钥 #11 解密结果: IBSTIJM EBSKJ
    密钥 #12 解密结果: HARSHIL DARJI
    密钥 #13 解密结果: GZQRGHK CZQIH
    密钥 #14 解密结果: FYPQFGJ BYPHG
    密钥 #15 解密结果: EXOPEFI AXOGF
    密钥 #16 解密结果: DWNODEH ZWNFE
    密钥 #17 解密结果: CVMNCDG YVMED
    密钥 #18 解密结果: BULMBCF XULDC
    密钥 #19 解密结果: ATKLABE WTKCB
    密钥 #20 解密结果: ZSJKZAD VSJBA
    密钥 #21 解密结果: YRIJYZC URIAZ
    密钥 #22 解密结果: XQHIXYB TQHZY
    密钥 #23 解密结果: WPGHWXA SPGYX
    密钥 #24 解密结果: VOFGVWZ ROFXW
    密钥 #25 解密结果: UNEFUVY QNEWV
    """
    长度 = len(LETTERS)
    try:
        密钥表 = list().append(LETTERS.find(密钥表))
    except Exception as e:
        assert 密钥表 == 长度
    for 密钥 in range(密钥表):
        解密 = ""
        for 字符 in 信息:
            if 字符 in LETTERS:
                序号 = LETTERS.find(字符)
                序号 = (序号 + 长度 - 密钥)%长度
                解密 = 解密 + LETTERS[序号]
            else:
                解密 = 解密 + 字符
        print("密钥 #" + str(密钥) + " 解密结果: " + 解密)

def 蛮力凯撒密码():
    信息 = input("Encrypted 信息: ")
    信息 = 信息.upper()
    解码(信息)
brute_force_caesar_cipher = 蛮力凯撒密码

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    蛮力凯撒密码()
