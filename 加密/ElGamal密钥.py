import os, random, sys
import 素数检验 as 素数, 密码数学模块 as 密码数学

min_primitive_root = 3

# I have written my code naively same as definition of primitive root
# however every time I run this program, memory exceeded...
# so I used 4.80 Algorithm in Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
# and it seems to run nicely!

def 本原元(模):
    print("计算 p 的本原元 ...")
    g = 3
    while pow(g, 2, 模) == 1 or pow(g, 模, 模) == 1:
        g = random.randrange(3,模)
    return g

def 产生密钥(长度):
    """
        随机选择一个大素数p，且要求p-1有大素数因子。再选择一个模p的本原元α。将p和α公开。
        随机选择一个整数d作为密钥，2≤d≤p-2 。
        计算y=α**d mod p，取y为公钥。
    """
    print('初始化素数 p ...')
    p = 素数.产生大素数(长度)
    α = 本原元(p)  # one primitive root on modulo p.
    d = random.randrange(3, p)  # private_key -> have to be greater than 2 for safety.
    y = 密码数学.求模逆(pow(α, d, p), p)

    公钥, 私钥 = (长度, α, y, p), (长度, d)

    return 公钥, 私钥

def 创建密钥文件(文件名, 长度):
    if os.path.exists(文件名 + "公钥.txt") or os.path.exists(文件名 + "私钥.txt"):
        print('\n警告:')
        print('"' + 文件名 + '公钥.txt" 或 ' + 文件名 + '私钥.txt" 已经存在. \n请更改文件名或删除文件后再次运行此程序.')
        sys.exit()
    else:
        公钥, 私钥 = 产生密钥(长度)
        print('\n公钥写入' + 文件名 + '公钥.txt ...')
        with open(文件名 + "公钥.txt", 'w') as fo:
            fo.write('%d,%d,%d,%d' % (公钥[0], 公钥[1], 公钥[2], 公钥[3]))

        print('私钥写入 ' + 文件名 + '私钥.txt"...')
        with open(文件名 + "私钥.txt", 'w') as fo:
            fo.write('%d,%d' % (私钥[0], 私钥[1]))

def ElGamal密钥():
    """
        对于明文M加密:
            随机地选取一个整数k，2≤k≤p-2。
            C1＝α^k mod  p；
            C2＝MY^k mod  p；
            密文为（C1,C2）
        由密文可得明文M:
            M=C2/C1^d mod p
    """
    print('创建elgamal密钥文件 ..')
    创建密钥文件('elgamal', 2048)
    print('密钥文件已成功初始化.')

if __name__ == '__main__':
    ElGamal密钥()
