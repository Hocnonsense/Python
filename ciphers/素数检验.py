
#import rabin_miller as rabin Miller
# Primality Testing with the Rabin-Miller Algorithm
"""
Fermat小定理的Euler推广:
            如果p是素数，a是小于p的正整数，那么a^(p-1) mod p = 1。
    证明：
            如果p是一个素数的话，那么对任意一个小于p的正整数a，a, 2a, 3a, …, (p-1)a除以p的余数正好是一个1到p-1的排列。
        反证法，假如结论不成立的话，那么就是说有两个小于p的正整数m和n使得na和ma除以p的余数相同。
        不妨假设n>m，则p可以整除a(n-m)。但p是素数，那么a和n-m中至少有一个含有因子p。这显然是不可能的，因为a和n-m都比p小。
        用同余式表述，我们证明了：
            (p-1)! ≡ a * 2a * 3a * … * (p-1)a (mod p)
        也即：
            (p-1)! ≡ (p-1)! * a^(p-1) (mod p)
    　　两边同时除以(p-1)!，就得到了我们的最终结论：
            1 ≡ a^(p-1) (mod p)

Miller-Rabin素性测试算法依据定理:
            如果p是素数，x是小于p的正整数，且x^2 mod p = 1，那么要么x=1，要么x=p-1。
        Miller-Rabin 素性测试同样是不确定算法，我们把可以通过以a为底的Miller-Rabin测试的合数称作以a为底的强伪素数(strong pseudoprime)。
        第一个以2为底的强伪素数为2047。第一个以2和3为底的强伪素数则大到1 373 653。

"""

import random

lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
             61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
             131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
             193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
             263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
             337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
             409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
             479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
             569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
             641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
             719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
             809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
             881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
             971, 977, 983, 991, 997]

def 素数检验(随机数):
    s, t = 随机数 - 1, 0

    while s % 2 == 0:
        s = s // 2
        t += 1  #随机数 == s*(2^t)+1, s 是奇数
    for trials in range(5):
        a = random.randrange(2, 随机数 - 1)    # 随机选取 5 个底数
        v = pow(a, s, 随机数)
        if v != 1:
            for i in range(t):          # i = 0
                if v == 随机数 - 1:      # while v != (随机数 - 1):
                    break               #     if i == t - 1:
                else:                   #         return False
                    v = (v**2) % 随机数  #     else:
            else:   # if i == t - 1:    #         i += 1
                return False            #         v = (v ** 2) % 随机数
    return True

def 是素数(随机数):
    """
        共进行四次检验
    """
    if (随机数 < 2):
        return False
    elif 随机数 in lowPrimes:
        return True
    else:
        #if (随机数 > lowPrimes[-1]): print("无法确定是否是素数")
        for prime in lowPrimes:
            if (随机数 % prime) == 0:
                return False
        return 素数检验(随机数)

#def generateLargePrime
def 产生大素数(长度 = 1024):
    while True:
        随机数 = random.randrange(2 ** (长度 - 1), 2 ** (长度))
        if 是素数(随机数):
            return 随机数

if __name__ == '__main__':
    随机数 = 产生素数()
    print(('素数是: ', 随机数))
    print(('是素数: ', 是素数(随机数)))
