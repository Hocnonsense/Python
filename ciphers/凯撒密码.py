def 加密(字串, 密钥):
    密文 = ''
    for x in 字串:
        字符 = (ord(x) + 密钥) % 256
        if 字符 > 126:
            字符 = 字符 - 95
        密文 = 密文 + chr(字符)
    return 密文

def 解密(字串, 密钥):
    明文 = ''
    for x in 字串:
        字符 = (ord(x) - 密钥) % 256
        if 字符 < 32:
            字符 = 字符 + 95
        明文 = 明文 + chr(字符)
    return 明文

def 蛮力破解(字串):
    密钥 = 1
    明文 = ''
    while 密钥 <= 94:
        for x in 字串:
            字符 = (ord(x) - 密钥) % 256
            if 字符 < 32:
                字符 = 字符 + 95
            明文 = 明文 + chr(字符)
        print("密钥: {}\t| Message: {}".format(密钥, 明文))
        明文 = ''
        密钥 += 1
    return None

def 凯撒密码():
    while True:
        print('-' * 10 + "\n**选项**\n" + '-' * 10)
        print("1.加密")
        print("2.解密")
        print("3.蛮力破解")
        print("4.退出")
        选项 = input("请输入你的选择: ")
        if 选项 not in ['1', '2', '3', '4']:
            print("输入无效, 请选择有效输入")
        elif 选项 == '1':
            字串 = input("请输入需要加密的字串: ")
            密钥 = int(input("请输入 1-94 之间的密钥, 将用于移位: "))
            if 密钥 in range(1, 95):
                print(加密(字串.lower(), 密钥))
            else:
                print("输入无效, 请选择有效输入")
        elif 选项 == '2':
            字串 = input("请输入需要解密的字串: ")
            密钥 = int(input("请输入 1-94 之间的密钥, 将用于移位: "))
            if 密钥 in range(1,95):
                print(解密(字串, 密钥))
            else:
                print("输入无效, 请选择有效输入")
        elif 选项 == '3':
            字串 = input("请输入需要解密的字串: ")
            蛮力破解(字串)
            凯撒密码()
        elif 选项 == '4':
            break
    print("再见.")
caesar_cipher = 凯撒密码


if __name__ == '__main__':
    凯撒密码()
