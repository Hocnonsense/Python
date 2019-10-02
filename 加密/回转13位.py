def 加密(s, n):
    out = ''
    for c in s:
        if c >= 'A' and c <= 'Z':
            out += chr(ord('A') + (ord(c) - ord('A') + n) % 26)
        elif c >= 'a' and c <= 'z':
            out += chr(ord('a') + (ord(c) - ord('a') + n) % 26)
        else:
            out += c
    return out
def 解密(s, n):
    加密(s, 26 - n)

def 回转13位():
    """
        仅仅只需要检查字母顺序并取代它在13位之后的对应字母，有需要超过时则重新绕回26英文字母开头即可。
            A换成N、B换成O、依此类推到M换成Z, 
            N换成A、O换成B、最后Z换成M。
        数字、符号、空白字符以及所有其他字符都不变。替换后的字母大小写保持不变。
    """
    s0 = 'HELLO'
    key = 13
    s1 = 加密(s0, key)
    print(s1)  # URYYB
    s2 = 加密(s1, key)
    print(s2)  # HELLO
rot13 = 回转13位

if __name__ == '__main__':
    回转13位()
