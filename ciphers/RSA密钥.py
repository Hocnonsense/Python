import random, os
import 素数检验 as 素数, 密码数学模块 as 密码数学

def 产生密钥(长度):
    """
        N:  N＝ p ＊ q ；p，q为质数
        L:  L＝lcm（p－1，q－1） ；L为p－1、q－1的最小公倍数
        E:  1 < E < L，gcd（E，L）=1；E，L最大公约数为1（E和L互质）
        D:  1 < D < L，E＊D mod L ＝ 1
    """
    print('初始化素数 p 和 q ...')
    p, q = 素数.产生大素数(长度), 素数.产生大素数(长度)
    n, l = p * q, (p - 1) * (q - 1)

    print('初始化与 (p - 1) * (q - 1) 互素的数 e ...')
    e = 0
    while 密码数学.最小公约数(e, l) != 1:
        e = random.randrange(2 ** (长度 - 1), 2 ** (长度))

    print('计算 e 的模逆 d ...')
    d = 密码数学.求模逆(e, l)

    公钥, 私钥 = (n, e), (n, d)
    return (公钥, 私钥)

def 创建密钥文件(文件名, 密钥长度):
    """
        创建 '文件名 + "公钥.txt"' 和 '文件名 + "私钥.txt"' 两个文件
        rsa算法初始化的时候一般要填入密钥长度,在96-1024bits间
            (1)加密1byte的明文,需要至少1+11=12bytes的密钥(不懂?看下面的明文长度),低于下限96bits时,一个byte都加密不了,当然没意义啦
            (2)这是算法本身决定的...当然如果某天网上出现了支持2048bits长的密钥的rsa算法时,你当我废话吧
    """
    if 密钥长度 < 96:
        raise Exception('密钥长度必须 > 96 . 请重新设置密钥长度')
    elif os.path.exists(文件名 + "公钥.txt") or os.path.exists(文件名 + "私钥.txt"):
        raise Exception('\n警告:"' + 文件名 + '公钥.txt" 或 ' + 文件名 + '私钥.txt" 已经存在. \n请更改文件名或删除文件后再次运行此程序.')
    else:
        公钥, 私钥 = 产生密钥(密钥长度)
        print('\n公钥写入 ' + 文件名 + '公钥.txt" ...')
        with open(文件名 + "公钥.txt", 'w') as fo:
            fo.write('%s,%s,%s' % (密钥长度, 公钥[0], 公钥[1]))

        print('私钥写入 ' + 文件名 + '私钥.txt"...')
        with open(文件名 + "私钥.txt", 'w') as fo:
            fo.write('%s,%s,%s' % (密钥长度, 私钥[0], 私钥[1]))
    return 文件名 + "公钥.txt", 文件名 + "私钥.txt"
makeKeyFiles = 创建密钥文件

def RSA密钥():
    """
        密文＝(明文**E)(mod N)
            也就是说RSA加密是对明文的E次方后除以N后求余数的过程
        明文＝(密文**D)(mod N)
            也就是说对密文进行D次方后除以N的余数就是明文
    """
    print('创建RSA密钥文件 ...')
    文件名 = 创建密钥文件('RSA', 1024)
    print('密钥文件 ' + 文件名[0] + ' 和 ' + 文件名[1] + ' 已成功初始化.')
rsa_key_generator = RSA密钥

if __name__ == '__main__':
    RSA密钥()
