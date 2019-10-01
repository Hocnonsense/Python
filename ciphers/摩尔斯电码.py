# Python program to implement Morse Code Translator
# Dictionary representing the morse code chart

摩尔斯电码表 = { 
    'A':'.-',   'B':'-...', 'C':'-.-.',
    'D':'-..',  'E':'.',    'F':'..-.',
    'G':'--.',  'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-',  'L':'.-..',
    'M':'--',   'N':'-.',   'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.',
    'S':'...',  'T':'-',    'U':'..-',
    'V':'...-', 'W':'.--',  'X':'-..-',
    'Y':'-.--', 'Z':'--..',
    '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
    '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
    ', ':'--..--',  '.':'.-.-.-',   '?':'..--..',   '/':'-..-.',    '-':'-....-',   '(':'-.--.',    ')':'-.--.-'
}

def 加密(信息):
    密文 = ''
    for 字符 in 信息:
        if 字符 != ' ':
            密文 += 摩尔斯电码表[字符] + ' '
        else:
            密文 += ' '
    return 密文

def 解密(信息):
    信息 += ' '
    明文 = ''
    电码 = ''
    for 字符 in 信息:
        if (字符 != ' '):
            分隔符 = 0
            电码 += 字符
        else:
            分隔符 += 1
            if 分隔符 == 1:
                明文 += list(摩尔斯电码表.keys())[list(摩尔斯电码表.values()).index(电码)]
                电码 = ''
            elif 分隔符 == 2 :
                明文 += ' '
    return 明文

def 摩尔斯电码():
    信息 = input("请输入您的报文: ") # "morse code here"  # 
    报文 = 加密(信息.upper())
    print(报文)
    信息 = 报文
    报文 = 解密(信息)
    print(报文)
morse_code_implementation = 摩尔斯电码

if __name__ == '__main__':
    摩尔斯电码()
