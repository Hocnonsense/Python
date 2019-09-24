import random, sys, os
import 素数检验 as 素数, 密码数学模块 as 密码数学

def generateKey(keySize):
    print('Generating prime p...')
    p = 素数.产生大素数(keySize)
    print('Generating prime q...')
    q = 素数.产生大素数(keySize)
    n = p * q

    print('Generating e that is relatively prime to (p - 1) * (q - 1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if 密码数学.最小公约数(e, (p - 1) * (q - 1)) == 1:
            break

    print('Calculating d that is mod inverse of e...')
    d = 密码数学.求模逆(e, (p - 1) * (q - 1))

    公钥 = (n, e)
    私钥 = (n, d)
    return (公钥, 私钥)

def makeKeyFiles(name, keySize):
    if os.path.exists(name + "公钥.txt") or os.path.exists(name + "私钥.txt"):
        print('\n警告:')
        print('"' + name + '公钥.txt" 或 ' + name + '私钥.txt" 已经存在. \n请更改文件名或删除文件后再次运行此程序.')
        sys.exit()
    else:
        公钥, 私钥 = generateKey(keySize)
        print('\n公钥写入 ' + name + '公钥.txt" ...')
        with open(name + "公钥.txt", 'w') as fo:
            fo.write('%s,%s,%s' % (keySize, 公钥[0], 公钥[1]))

        print('私钥写入 ' + name + '私钥.txt"...')
        with open(name + "私钥.txt", 'w') as fo:
            fo.write('%s,%s,%s' % (keySize, 私钥[0], 私钥[1]))

def main():
    print('Making key files...')
    makeKeyFiles('rsa', 1024)
    print('Key files generation successful.')

if __name__ == '__main__':
    main()
