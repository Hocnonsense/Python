"""
	Peak signal-to-noise ratio - PSNR - https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
    Soruce: https://tutorials.techonical.com/how-to-calculate-psnr-value-of-two-images-using-python/

    一个信号的峰值信噪比（psnr）是一个信号的最大功率与可能影响它的表示精度的噪声功率的比值，也就是max 
    控制quality下降，同时可以看到图片逐渐模糊，相应的psnr也也随之下降，符合我们的主观期望。 
然而有这种评估算法也存在着一些缺陷。由它的定义我们可以完全看出这是一种非常objective的评估，并没有在它的模型中引入与人肉眼相关的一些参量。例如人总是对颜色与亮度的变化，有着很高的敏感度，如果在压缩时我们有针对的只去破环了这些部分，那么即使有很高的psnr，人眼对于这种重建的期望或许就与psnr反应的预期期望有着很大的误差。
原文链接：https://blog.csdn.net/texas_instrument/article/details/74853321
"""

import math, os, cv2
import numpy as np

def psnr(original, contrast):
    mse = np.mean((original - contrast) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


def main():
    # 把图像放在非中文路径进行读取后，就没问题了。
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    print(os.path.join(dir_path, 'image_data\\original_image.png'))
    # Loading images (original image and compressed image)
    original = cv2.imread(os.path.join(dir_path, 'image_data\\original_image.png'))
    contrast = cv2.imread(os.path.join(dir_path, 'image_data\\compressed_image.png'), 1)

    original2 = cv2.imread(os.path.join(dir_path, 'image_data\\PSNR-example-base.png'))
    contrast2 = cv2.imread(os.path.join(dir_path, 'image_data\\PSNR-example-comp-10.jpg'), 1)
    cv2.imshow("1", contrast2)

    # Value expected: 29.73dB
    print("-- First Test --")
    print(f"PSNR value is {psnr(original, contrast)} dB")

    # # Value expected: 31.53dB (Wikipedia Example)
    print("\n-- Second Test --")
    print(f"PSNR value is {psnr(original2, contrast2)} dB")


if __name__ == '__main__':
    main()
