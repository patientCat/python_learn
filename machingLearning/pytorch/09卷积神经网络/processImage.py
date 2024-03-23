
"""
给定一个图像，进行处理
"""
import numpy
from PIL import Image
import numpy as np
from typing import Optional


cat_image = Image.open("../data/cat_download.jpeg")
array = np.array(cat_image)
print(array.shape)


# 卷积
def numpy_conv(data : np.array, targetConv : Optional[np.array], kernel_size=3):
    final_kernel_size = 0
    final_kernel = None
    if targetConv is not None:
        # 指定卷积核
        final_kernel = targetConv
        final_kernel_size = final_kernel.shape[0]
    else:
        final_kernel_size = kernel_size
        ones = numpy.ones((kernel_size, kernel_size)) / (kernel_size * kernel_size)
        final_kernel = ones
        """
        [1, 2, 3, 4]      [1, 1, 1]
        [4, 5, 6, 4] conv [1, 1, 1] = 
        [7, 8, 9, 4]      [1, 1, 1]
        [1, 2, 3, 4] 
        """
    Hsize = data.shape[0]
    Wsize = data.shape[1]
    print(f"Hsize={Hsize}, Wsize={Wsize}")
    Hsize_out = Hsize - final_kernel_size + 1
    Wsize_out = Wsize - final_kernel_size + 1
    print(f"HsizeOut={Hsize_out}, WsizeOut={Wsize_out}")
    zeros_out = np.zeros((Hsize_out, Wsize_out), dtype=np.uint8)
    for i in range(Hsize_out):
        for j in range(Wsize_out):
            sum_v = 0
            for m in range(kernel_size):
                for n in range(kernel_size):
                    sum_v = sum_v + final_kernel[m][n] * data[i+m][j+n]
            zeros_out[i][j] = sum_v
    #print(zeros_out)
    return zeros_out

channel1 = array[:, :, 0]
print(channel1.shape)
channel1_after_conv = numpy_conv(channel1, None, 10)

print("process_channel1")
print(channel1)
data = Image.fromarray(channel1)
data.save("channel1.jpg")

print("process_channel1_after_conv")
print(channel1_after_conv)
data_after_conv = Image.fromarray(channel1_after_conv)
data_after_conv.save("channel1_after_conv.jpg")

# 从结果图片上可以直接看到卷积后的结果
channel2_after_conv = numpy_conv(channel1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
print("process_channel2_after_conv")
data_after_conv = Image.fromarray(channel2_after_conv)
data_after_conv.save("channel2_after_conv.jpg")


channel3_after_conv = numpy_conv(channel1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
print("process_channel3_after_conv")
data_after_conv = Image.fromarray(channel3_after_conv)
data_after_conv.save("channel3_after_conv.jpg")
