"""
    base64编码的原理是先将源文件以标准字节（byte）为单位转化成二进制，一个字节占8个位（bit），如“ABC”的二进制是01000001、01000010、01000011，这样源文件就形成了每8个bit一组的一串二进制，然后将这些二进制串以base64特有的规则（每个字节占6个位）再转化成base64格式的字符，编码完成。解码就是这个过程反过来。
原文链接：https://blog.csdn.net/zm342021666/article/details/77461528
"""


base64字符表 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodeBase64(text):
    """
        编码前，在源文件的前后分别加上干扰字符，
        为了增加破译的难度，这些字符可以稍微复杂点，
        但是要提前告知服务端加密的格式，这样服务端才能在解码时排除干扰字符得到正确的内容。
    """
    c = 3 - len(text) % 3 #the length of padding
    s = text + "\0" * c #the text to encode
    
    输出, i = "", 0 #the result
    while i < len(s):
        if i > 0 and ((i / 3 * 4) % 76) == 0:
            输出 += "\r\n"

        n = (ord(s[i]) << 16) + (ord(s[i+1]) << 8 ) + ord(s[i+2])
        
        n1 = (n >> 18) & 63
        n2 = (n >> 12) & 63
        n3 = (n >> 6)  & 63
        n4 = n & 63

        输出 += base64字符表[n1] + base64字符表[n2] + base64字符表[n3] + base64字符表[n4]
        i += 3

    return 输出[0: len(输出)-c] + "=" * c # p = "="*c #the padding

def decodeBase64(text):
    s = ""

    for i in text:
        if i in base64字符表:
            s += i
            c = 0
        elif i == '=':  # 计算末尾的 '=' 数量
            c += 1
    s = s + "A"*c

    输出, i = "", 0 #the result
    while i < len(s):
        n = (base64字符表.index(s[i]) << 18) + (base64字符表.index(s[i+1]) << 12) + (base64字符表.index(s[i+2]) << 6) + base64字符表.index(s[i+3])
        输出 += chr((n >> 16) & 255) + chr((n >> 8) & 255) + chr(n & 255)
        i += 4

    return 输出[0: len(输出) - c]

if __name__ == '__main__':
    print(encodeBase64("WELCOME to base64 encoding"))
    print(decodeBase64(encodeBase64("WELCOME to base64 encoding")))