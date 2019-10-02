字符集 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def 检查密钥(密钥):
    密钥表 = list(密钥)
    字符表 = list(字符集)
    密钥表.sort()
    字符表.sort()
    if 密钥表 != 字符表:
        raise Exception('密钥错误或字符表错误.')

def 产生密钥(字符表 = 字符集):
    import random
    密钥 = list(字符表)
    random.shuffle(密钥)
    return ''.join(密钥)

def translateMessage(密钥, 信息, 模式):
    加密信息 = ''
    charsA = 字符集
    charsB = 密钥

    if 模式 == '解密':
        charsA, charsB = charsB, charsA

    for 字符 in 信息:
        if 字符.upper() in charsA:
            字符序号 = charsA.find(字符.upper())
            if 字符.isupper():
                加密信息 += charsB[字符序号].upper()
            else:
                加密信息 += charsB[字符序号].lower()
        else:
            加密信息 += 字符

    return 加密信息

def 加密(密钥, 信息):
    """
    >>> 加密('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translateMessage(密钥, 信息, '加密')

def 解密(密钥, 信息):
    """
    >>> 解密('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return translateMessage(密钥, 信息, '解密')

def 简单替换加密():
    模式 = input('加密/解密 [e/d]: ')
    
    if 模式.lower().startswith('e'):
        模式 = '加密'
        密钥 = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'   # 产生密钥() # 
    elif 模式.lower().startswith('d'):
        模式 = '解密'
        密钥 = input("输入密钥: ")
    检查密钥(密钥)
    信息 = input('输入需要' + 模式 + '的信息: ')

    if 模式 == '加密':
        信息 = 加密(密钥, 信息)
    elif 模式 == '解密':
        信息 = 解密(密钥, 信息)
    print('\n%s结果: \n%s' % (模式.title(), 信息))
simple_substitution_cipher = 简单替换加密

if __name__ == '__main__':
    简单替换加密()
