import os
import RSA密钥 as rkg

默认片长 = 128
字节大小 = 256

def 读取密钥文件(密钥文件名):
    with open(密钥文件名) as 文件:
        文件内容 = 文件.read()
    密钥长度, n, EorD = 文件内容.split(',')
    return (int(密钥长度), (int(n), int(EorD)))

def 信息分片(信息, 片长 = 默认片长):
    二进制信息 = 信息.encode('ascii')
    片转整数表 = list()
    for 片起始 in range(0, len(二进制信息), 片长):
        片转整数 = 0
        片结束 = min(片起始 + 片长, len(二进制信息))
        for i in range(片起始, 片结束):
            片转整数 += 二进制信息[i] * (字节大小 ** (i % 片长))
        片转整数表.append(片转整数)
    return 片转整数表

def 加密信息(信息, 密钥, 片长=默认片长):
    加密片, (n, e) = list(), 密钥
    for 片 in 信息分片(信息, 片长):
        加密片.append(pow(片, e, n))
    return 加密片

def 加密并保存(密文文件名, 公钥文件名, 信息, 片长 = 默认片长):
    密钥长度, 密钥 = 读取密钥文件(公钥文件名)
    if 密钥长度 < 片长 * 8 - 11:
        raise Exception('ERROR: 请减少数据块大小或者增加密钥长度.\n块大小为 ' + str(片长 * 8) + ' 位，密钥大小为 ' + str(密钥长度) + ' 位。')
    else:
        加密片 = 加密信息(信息, 密钥, 片长)
        for i in range(len(加密片)):
            加密片[i] = str(加密片[i])
        加密内容 = '%s_%s_%s' % (len(信息), 片长, ','.join(加密片))
        with open(密文文件名, 'w') as 文件:
            文件.write(加密内容)
        return 加密内容

def 片转信息(片转整数表, 信息长度, 片长 = 默认片长):
    信息 = list()
    for 片转整数 in 片转整数表:
        片内信息 = list()
        for i in range(片长 - 1, -1, -1):
            if len(信息) + i < 信息长度:
                二进制信息 = 片转整数 // (字节大小 ** i)
                片转整数 = 片转整数 % (字节大小 ** i)
                片内信息.insert(0, chr(二进制信息))
        信息.extend(片内信息)
    return ''.join(信息)

def 解密信息(加密片, 信息长度, 密钥, 片长 = 默认片长):
    解密片 = list()
    n, d = 密钥
    for 片 in 加密片:
        解密片.append(pow(片, d, n))
    return 片转信息(解密片, 信息长度, 片长)

def 读取并解密(密文文件名, 公钥文件名):
    密钥长度, 密钥 = 读取密钥文件(公钥文件名)
    with open(密文文件名) as 文件:
        文件内容 = 文件.read()
    信息长度, 片长, 加密信息 = 文件内容.split('_')
    信息长度 = int(信息长度)
    片长 = int(片长)
    if 密钥长度 < 片长 * 8 - 11:
        raise Exception('ERROR: 你是否指定了正确的密钥文件和加密文件?\n块大小为 ' + str(片长 * 8) + ' 位，密钥大小为 ' + str(密钥长度) + ' 位。')
    else:
        加密片 = list()
        for 片 in 加密信息.split(','):
            加密片.append(int(片))
        return 解密信息(加密片, 信息长度, 密钥, 片长)

def RSA加密():
    文件名 = 'rsa加密文件.txt'
    模式 = input(r'加密\解密 [e\d]: ')

    if 模式.lower().startswith('e'):
        模式 = '加密'
    elif 模式.lower().startswith('d'):
        模式 = '解密'

    if 模式 == '加密':
        公钥文件名 = 'rsa公钥.txt'
        if not os.path.exists(公钥文件名):
            公钥文件名 = rkg.创建密钥文件('rsa', 1024)[0]

        信息 = input('\n输入信息: ')
        print('加密并写入 ' + 文件名 + ' 中...')
        加密内容 = 加密并保存(文件名, 公钥文件名, 信息)

        print('\n加密后内容为:')
        print(加密内容)

    elif 模式 == '解密':
        私钥文件名 = 'rsa私钥.txt'
        print('从' + 文件名 + '读取并解密中...')
        解密信息 = 读取并解密(文件名, 私钥文件名)
        print('将解密信息写入 rsa解密文件.txt 中...')
        with open('rsa解密文件.txt', 'w') as 文件:
            文件.write(解密信息)
        print('\n解密信息: ')
        print(解密信息)
rsa_cipher = RSA加密

if __name__ == '__main__':
    RSA加密()
