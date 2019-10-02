import time, os
import 置换加密 as transCipher

def 文件置换加密():
    读取文件名 = 'Prehistoric Men.txt'
    输出文件名 = '输出.txt'
    密钥 = int(input('输入密钥: '))
    模式 = input('加密/解密 [e/d]: ')

    if not os.path.exists(读取文件名):
        raise Exception(读取文件名 + '不存在. 程序已退出...')
    else:
        if os.path.exists(输出文件名):
            print('Overwrite %s? [y/n]' % 输出文件名)
            response = input('> ')
            if not response.lower().startswith('y'):
                raise Exception('无法写入文件. sys.exit()')
        elif 模式 == '解密':
            raise Exception(输出文件名 + '不存在. ')
        起始时间 = time.time()
        if 模式.lower().startswith('e'):
            with open(读取文件名) as 文件:
                文件内容 = 文件.read()
            译文 = transCipher.加密(密钥, 文件内容)
        elif 模式.lower().startswith('d'):
            with open(输出文件名) as 文件:
                文件内容 = 文件.read()
            译文 =transCipher .解密(密钥, 文件内容)

        with open(输出文件名, 'w') as 输出文件:
            输出文件.write(译文)

        处理时间 = round(time.time() - 起始时间, 2)
        print(('处理共花费 ' + 处理时间 + ' 秒. '))
transposition_cipher_encrypt_decrypt_file = 文件置换加密

if __name__ == '__main__':
    文件置换加密()
