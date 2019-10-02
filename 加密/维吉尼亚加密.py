字母表 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(密钥, 信息, 模式):
    译文 = list()
    对应密钥 = 0
    密钥 = 密钥.upper()

    for 字符 in 信息:
        序号 = 字母表.find(字符.upper())
        if 序号 != -1:
            if 模式 == '加密':
                序号 += 字母表.find(密钥[对应密钥])
            elif 模式 == '解密':
                序号 -= 字母表.find(密钥[对应密钥])

            序号 %= len(字母表)

            if 字符.isupper():
                译文.append(字母表[序号])
            elif 字符.islower():
                译文.append(字母表[序号].lower())

            对应密钥 += 1
            if 对应密钥 == len(密钥):
                对应密钥 = 0
        else:
            译文.append(字符)
    return ''.join(译文)

def 加密(密钥, 信息):
    '''
    >>> 加密('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    '''
    return translateMessage(密钥, 信息, '加密')

def 解密(密钥, 信息):
    '''
    >>> 解密('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    '''
    return translateMessage(密钥, 信息, '解密')

def 维吉尼亚加密():
    信息 = input('输入信息: ')
    密钥 = input('输入密钥 [字符串]: ')
    模式 = input('加密/解密 [e/d]: ')

    if 模式.lower().startswith('e'):
        模式 = '加密'
        译文 = 加密(密钥, 信息)
    elif 模式.lower().startswith('d'):
        模式 = '解密'
        译文 = 解密(密钥, 信息)

    print('\n%sed 信息:' % 模式.title())
    print(译文)
vigenere_cipher = 维吉尼亚加密

if __name__ == '__main__':
    维吉尼亚加密()

"""
如何破解Vigenere密码:
    第一步：位移法求解key的长度
        改变key的长度, 统计中相同字符出现的次数. 每次位移后计算与原密文对应相同的字母个数，即s[i]==s[i+key]，i为位置，j为位移量
    第二步：获取key长度之后，将文本分为key长度份，接下来将每份进行频率分析(Frequency Analysis)
    第三步：得到密钥, 破解

"""