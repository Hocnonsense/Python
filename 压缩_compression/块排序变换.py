"""
https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding. More importantly, the transformation is reversible, without needing to store any additional data except the position of the first original character. The BWT is thus a "free" method of improving the efficiency of text compression algorithms, costing only some extra computation.

Burrows-Wheeler 变换 (BWT, 也称为块排序压缩) 将字符串重新排列为相似字符的串。
这对于压缩非常有用, 因为通过移动到前端转换和游程长度编码等技术, 可以很容易地压缩具有重复字符串的字符串。
更重要的是, 变换是可逆的, 不需要存储除了第一个原始字符的位置之外的任何附加数据。
因此, BWT是一种提高文本压缩算法效率的“免费”方法, 只需要一些额外的计算。
Burrows-Wheeler变换(bwt, 也称为块排序压缩)。


扩展 Burrows-Wheeler 算法基本原理
设 D 为一个有序字母表, 在 D 上定义一个有限字符序列 (有时也称为单词) u = d1 d2…dn. 全部定义在 D 上的序列构成一个集合, 记为 D*. 设a, b 属于D* , 如果存在 m, n 属于D* 使得 a = mn 以及b = mn, 则称 a 是 b 的一个循环位移, 也可称 a与 b 是共轭的, 记为 a ~ b.  若有 n 属于 D* ,  且 n =mk ? n = m, k = 1 , 则称 n 为素词. 因为 D 是一个有序的字母集合, 所以在 D* 中任意两个不同的单词都可以按一定的顺序比较先后,  我们称 D*为全序集合. 设 m 属于 D* , 令 mu = mmmm…, 则 mu 是一个定义在 D 上的无限词.  为判断两个无限词的序关系, 可采用字典顺序. 假设给定两个无限词 α =α1α2α3… 以及 β = β1 β2 β3…, α < lexβ 意味着存在j 使得 αi = βi, i = 1, 2, …, j － 1, 且有 αj = βj.  取定两个素词 p, q 属于D* , 其中 q ? Cp, 利用Burrows-Wheeler 变换, 分别得到 p, q 对应的共轭等价类 Cp 和 Cq. 易知, Cp ∩Cq = φ .  令 Sp, q = Cp ∪ Cq .  Sp, q 按照 < ω 序关系构成一个全序集.  用 0和 1 分别标记 Sp, q 中属于 Cp 和 Cq 的元素. 将 DNA 序列看成字母集 D = {A, C, G, T }上的一个词.
"""
from typing import List, Dict

def 全部循环重排(信息: str) -> List[str]:
    """
    :param 信息: 一段字符串.
    :return: 一个列表. 逐个将第一个字符转移到字符串最后.
    :raises TypeError: 如果信息不是字符串
    Examples:

    >>> 全部循环重排("1234567") # doctest: +NORMALIZE_WHITESPACE
    ['1234567', '2345671', '3456712', '4567123', '5671234', '6712345', '7123456']
    >>> 全部循环重排(5)
    Traceback (most recent call last):
        ...
    TypeError: 信息应为字符串.
    """
    if not isinstance(信息, str):
        raise TypeError("信息应为字符串.")
    else:
        return [信息[i:] + 信息[:i] for i in range(len(信息))]

def 块排序压缩(信息: str) -> Dict:
    """
    :param 信息: The string that will be used at bwt algorithm
    :return: the string composed of the last char of each row of the ordered 循环重排 and the index of the original string at ordered 循环重排 list
    :raises TypeError: 如果信息不是字符串
    :raises ValueError: 如果信息是空串
    Examples:

    >>> 块排序压缩("^BANANA")
    {'块排序压缩信息': 'BNN^AAA', '原信息序号': 6}
    >>> 块排序压缩("a_asa_da_casa")
    {'块排序压缩信息': 'aaaadss_c__aa', '原信息序号': 3}
    >>> 块排序压缩("panamabanana")
    {'块排序压缩信息': 'mnpbnnaaaaaa', '原信息序号': 11}
    >>> 块排序压缩(4)
    Traceback (most recent call last):
        ...
    TypeError: 信息应为字符串.
    >>> 块排序压缩('')
    Traceback (most recent call last):
        ...
    ValueError: 输入信息必须非空.
    """
    if not isinstance(信息, str):
        raise TypeError("信息应为字符串.")
    elif not 信息:
        raise ValueError("输入信息必须非空.")
    else:
        循环重排 = 全部循环重排(信息)
        循环重排.sort()  # 按首字母字母表顺序重排循环重排
        return {
            "块排序压缩信息": "".join([word[-1] for word in 循环重排]), # 选取排序后的每个全循环字符串的最后一个字母练成的字符串
            "原信息序号": 循环重排.index(信息),  # 报告哪个是原字符串(如果在信息末尾添加 \EOF, 则不需要
        }

def 逆块排序压缩(块排序压缩信息: str, 原信息序号: int, 想知道为什么 = False) -> str:
    """
    :param 块排序压缩信息: The string returned from bwt algorithm execution
    :param 原信息序号: A 0-based index of the string that was used to
    generate 块排序压缩信息 at ordered 循环重排 list
    :return: The string used to generate 块排序压缩信息 when bwt was executed
    :raises TypeError: If the 块排序压缩信息 parameter type is not str
    :raises ValueError: If the 块排序压缩信息 parameter is empty
    :raises TypeError: If the 原信息序号 type is not int or if not
    possible to cast it to int
    :raises ValueError: If the 原信息序号 value is lower than 0 or
    greater than len(块排序压缩信息) - 1

    >>> 逆块排序压缩("BNN^AAA", 6)
    '^BANANA'
    >>> 逆块排序压缩("aaaadss_c__aa", 3)
    'a_asa_da_casa'
    >>> 逆块排序压缩("mnpbnnaaaaaa", 11)
    'panamabanana'
    >>> 逆块排序压缩(4, 11)
    Traceback (most recent call last):
        ...
    TypeError: 块排序压缩信息应为字符串.
    >>> 逆块排序压缩("", 11)
    Traceback (most recent call last):
        ...
    ValueError: 块排序压缩信息必须非空.
    >>> 逆块排序压缩("mnpbnnaaaaaa", "asd") # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    TypeError: 原信息序号必须能够转变为数字.
    >>> 逆块排序压缩("mnpbnnaaaaaa", -1)
    Traceback (most recent call last):
        ...
    ValueError: 原信息序号必须介于0和块排序压缩信息长度之间.
    >>> 逆块排序压缩("mnpbnnaaaaaa", 12) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: 原信息序号必须介于0和块排序压缩信息长度之间.
    >>> 逆块排序压缩("mnpbnnaaaaaa", 11.0)
    'panamabanana'
    >>> 逆块排序压缩("mnpbnnaaaaaa", 11.4)
    'panamabanana'
    """
    if not isinstance(块排序压缩信息, str):
        raise TypeError("块排序压缩信息应为字符串.")
    elif not 块排序压缩信息:
        raise ValueError("块排序压缩信息必须非空.")
    else:
        try:
            原信息序号 = int(原信息序号)
        except ValueError:
            raise TypeError("原信息序号必须能够转变为数字.")
        else:
            if 原信息序号 < 0 or 原信息序号 >= len(块排序压缩信息):
                raise ValueError("原信息序号必须介于0和块排序压缩信息长度之间.")
            else:
                循环重排 = [""] * len(块排序压缩信息)
                for x in range(len(块排序压缩信息)):
                    for i in range(len(块排序压缩信息)):
                        循环重排[i] = 块排序压缩信息[i] + 循环重排[i]
                    if 想知道为什么:
                        print(循环重排)
                    循环重排.sort()
                return 循环重排[原信息序号]

def 块排序变换():
    print("请输入一串字符, 我将用其演示 BWT 转换: ")
    信息 = input().strip()
    result = 块排序压缩(信息)
    print("块排序压缩将 '" + 信息  + "' 转变为了 '" + result["块排序压缩信息"] + "'")
    原始信息 = 逆块排序压缩(result["块排序压缩信息"], result["原信息序号"])
    print("逆块排序压缩 '" + result["块排序压缩信息"] + "' , 我们得到了初始字符串: '" + 原始信息 + "'")
Burrows_Wheeler_Transformation = 块排序变换

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    块排序变换()
