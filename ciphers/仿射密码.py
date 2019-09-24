import sys, random
import 密码数学模块 as 密码数学

密码表 = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def 分解密钥(密钥):
    keyA = 密钥 // len(密码表)
    keyB = 密钥 % len(密码表)
    return (keyA, keyB)

def 检查密钥(keyA, keyB, 模式):
    if keyA == 1 and 模式 == '加密':
        sys.exit('密钥 A 为 1 会降低加密强度. 请换一个密钥')
    elif keyB == 0 and 模式 == '加密':
        sys.exit('密钥 B 为 0 会降低加密强度. 请换一个密钥')
    elif keyA < 0 or keyB < 0 or keyB > len(密码表) - 1:
        sys.exit('密钥 A 必须是大于 0 的整数, 且密钥 B 必须在 0 到 ' + (len(密码表) - 1) + ' 之间')
    elif 密码数学.最小公约数(keyA, len(密码表)) != 1:
        sys.exit('密钥 A ' + keyA + ' 和密码表大小 ' + len(密码表) + ' 不是不可约的. 请换一个密钥')

def 加密信息(密钥, 信息):
    '''
    >>> 加密信息(4545, 'The affine cipher is a type of monoalphabetic substitution cipher.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    '''
    keyA, keyB = 分解密钥(密钥)
    检查密钥(keyA, keyB, '加密')
    密文 = ''
    for 字符 in 信息:
        if 字符 in 密码表:
            替换 = 密码表.find(字符)
            密文 += 密码表[(替换 * keyA + keyB) % len(密码表)]
        else:
            密文 += 字符
    return 密文

def 解密信息(密钥, 信息):
    '''
    >>> 解密信息(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi')
    'The affine cipher is a type of monoalphabetic substitution cipher.'
    '''
    keyA, keyB = 分解密钥(密钥)
    检查密钥(keyA, keyB, '解密')
    明文 = ''
    模逆 = 密码数学.求模逆(keyA, len(密码表))
    for 字符 in 信息:
        if 字符 in 密码表:
            替换 = 密码表.find(字符)
            明文 += 密码表[(替换 - keyB) * 模逆 % len(密码表)]
        else:
            明文 += 字符
    return 明文

def 随机密钥():
    while True:
        keyA = random.randint(2, len(密码表))
        keyB = random.randint(2, len(密码表))
        if 密码数学.最小公约数(keyA, len(密码表)) == 1:
            return keyA * len(密码表) + keyB

def 仿射密码():
    信息 = input('输入原始信息: ')
    密钥 = int(input('输入密钥 [2000 - 9000]: '))
    模式 = input('需要加密请输入"E", 需要解密请输入"D" [encrypt/decrypt]: ')

    if 模式.lower().startswith('e'):
              模式 = '加密'
              处理方式 = 加密信息
    elif 模式.lower().startswith('d'):
              模式 = '解密'
              处理方式 = 解密信息
    新信息 = 处理方式(密钥, 信息)
    print('\n{处理}后的信息: \n{信息}'.format(处理 = 模式.title(), 信息 = 新信息))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    仿射密码()
