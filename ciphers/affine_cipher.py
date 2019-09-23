import sys, random
import 密码数学模块 as 密码数学

SYMBOLS = r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def 分解密钥(密钥):
    keyA = 密钥 // len(SYMBOLS)
    keyB = 密钥 % len(SYMBOLS)
    return (keyA, keyB)

def 检查密钥(keyA, keyB, 模式):
    if keyA == 1 and 模式 == '加密':
        sys.exit('密钥 A 为 1 会降低加密强度. 请换一个密钥')
    elif keyB == 0 and 模式 == '加密':
        sys.exit('密钥 B 为 0 会降低加密强度. 请换一个密钥')
    elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('密钥 A 必须是大于 0 的整数, 且密钥 B 必须在 0 到 ' + (len(SYMBOLS) - 1) + ' 之间')
    elif 密码数学.最小公约数(keyA, len(SYMBOLS)) != 1:
        sys.exit('密钥 A %s and the symbol set size %s are not relatively prime. Choose a different 密钥.' % (keyA, len(SYMBOLS)))

def 加密信息(密钥, 信息):
    '''
    >>> 加密信息(4545, 'The affine cipher is a type of monoalphabetic substitution cipher.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    '''
    keyA, keyB = 分解密钥(密钥)
    检查密钥(keyA, keyB, '加密')
    cipherText = ''
    for symbol in 信息:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol
    return cipherText

def 解密信息(密钥, 信息):
    '''
    >>> 解密信息(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi')
    'The affine cipher is a type of monoalphabetic substitution cipher.'
    '''
    keyA, keyB = 分解密钥(密钥)
    检查密钥(keyA, keyB, '解密')
    plainText = ''
    modInverseOfkeyA = 密码数学.求模逆(keyA, len(SYMBOLS))
    for symbol in 信息:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symIndex - keyB) * modInverseOfkeyA % len(SYMBOLS)]
        else:
            plainText += symbol
    return plainText

def 随机密钥():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if 密码数学.最小公约数(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

def main():
    信息 = "message"#input('输入原始信息: ')
    密钥 = 8848#int(input('输入密钥 [2000 - 9000]: '))
    模式 = "end"#input('需要加密请输入"E", 需要解密请输入"D" [encrypt/decrypt]: ')

    if 模式.lower().startswith('e'):
              模式 = '加密'
              处理方式 = 加密信息
    elif 模式.lower().startswith('d'):
              模式 = '解密'
              处理方式 = 解密信息
    信息 = 处理方式(密钥, 信息)
    print('\n{处理}后的信息: \n{新信息}'.format(处理 = 模式.title(), 新信息 = 信息))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
