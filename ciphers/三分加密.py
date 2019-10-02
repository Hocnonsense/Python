#https://en.wikipedia.org/wiki/Trifid_cipher

def __预处理(信息, 字母表):
    #Validate 信息 and 字母表, set to upper and remove spaces
    字母表 = 字母表.replace(" ", "").upper()
    信息 = 信息.replace(" ", "").upper()

    #Check length and characters
    if len(字母表) != 27:
        raise KeyError("字母表大小应为27.")
    else:
        for 每个字符 in 信息:
            if 每个字符 not in 字母表:
                raise ValueError("输入的每个字符都需要在字母表中!")
        #Generate dictionares
        编号表 = ("111","112","113","121","122","123","131","132","133","211","212","213","221","222","223","231","232","233","311","312","313","321","322","323","331","332","333")
        字母转编号 = dict()
        编号转字母 = dict()
        for 字母, 编号 in zip(字母表, 编号表):
            字母转编号[字母] = 编号
            编号转字母[编号] = 字母

        return 信息, 字母表, 字母转编号, 编号转字母

def __加密片(信息片, 字母转编号):
    one, two, three = "", "", ""
    tmp = list()

    for character in 信息片:
        tmp.append(字母转编号[character])

    for 每个字符 in tmp:
        one += 每个字符[0]
        two += 每个字符[1]
        three += 每个字符[2]

    return one+two+three

def 加密(信息, 字母表 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    信息, 字母表, 字母转编号, 编号转字母 = __预处理(信息, 字母表)
    加密数字表 = ""
    for i in range(0, len(信息)+1, period):
        加密数字表 += __加密片(信息[i:i+period], 字母转编号)
    密文 = ""
    for i in range(0, len(加密数字表), 3):
        密文 += 编号转字母[加密数字表[i:i+3]]
    return 密文

def __解密片(信息片, 字母转编号):
    tmp, thisPart = "", ""
    result = list()

    for character in 信息片:
        thisPart += 字母转编号[character]

    for digit in thisPart:
        tmp += digit
        if len(tmp) == len(信息片):
            result.append(tmp)
            tmp = ""

    return result[0], result[1], result[2]

def 解密(信息, 字母表 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.", period=5):
    信息, 字母表, 字母转编号, 编号转字母 = __预处理(信息, 字母表)
    解密数字表 = list()
    明文 = ""

    for i in range(0, len(信息)+1, period):
        a,b,c = __解密片(信息[i:i+period], 字母转编号)

        for j in range(0, len(a)):
            解密数字表.append(a[j]+b[j]+c[j])

    for 每个字符 in 解密数字表:
        明文 += 编号转字母[每个字符]

    return 明文

def 三分加密():
    信息 = "DEFEND THE EAST WALL OF THE CASTLE."
    密文 = 加密(信息,"EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    明文 = 解密(密文, "EPSDUCVWYM.ZLKXNBTFGORIJHAQ")
    print("密文: {}\nDecrypted: {}".format(密文, 明文))
Trifid_cipher = 三分加密

if __name__ == '__main__':
    三分加密()