import math

def 加密(密钥, 信息):
    """
        将文本分为密钥个段落, 按每段的字符顺序重新排列:   
    >>> 加密(2, "123456")
    '135246'
    >>> 加密(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    密文 = [''] * 密钥
    for 列 in range(密钥):
        指针 = 列
        while 指针 < len(信息):
            密文[列] += 信息[指针]
            指针 += 密钥
    return ''.join(密文)

def 解密(密钥, 信息):
    """
    >>> 解密(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    列数 = math.ceil(len(信息) / 密钥)
    行数 = 密钥
    不足行数 = (列数 * 行数) - len(信息)
    明文 = [""] * 列数
    列, 行 = 0, 0

    for 字符 in 信息:
        明文[列] += 字符
        列 += 1

        if (列 == 列数) or ((列 == 列数 - 1) and (行 >= 行数 - 不足行数)):
            列 = 0
            行 += 1

    return "".join(明文)

def 置换加密():
    信息 = input('输入信息: ')
    密钥 = int(input('输入密钥[2-%s]: ' % (len(信息) - 1)))
    mode = input('加密/解密 [e/d]: ')

    if mode.lower().startswith('e'):
        信息 = 加密(密钥, 信息)
    elif mode.lower().startswith('d'):
        信息 = 解密(密钥, 信息)

    # Append pipe 字符 (vertical bar) to identify spaces at the end.
    print('输出:\n"""' + 信息 + '"""')
transposition_cipher = 置换加密

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    置换加密()
