def atbash():
    """
        最后一个字母代表第一个字母，倒数第二个字母代表第二个字母
    """
    输出=""
    for 字符 in input("请输入需要加密的字符: ").strip():
        UTF编码 = ord(字符)
        if 65 <= UTF编码 <= 90: # 大写字母
            输出 += chr(155-UTF编码)
        elif 97 <= UTF编码 <= 122:  # 小写字母
            输出 += chr(219-UTF编码)
        else:
            输出 += 字符
    print(输出)


if __name__ == '__main__':
    atbash()
