
"""
给定一个图像，进行处理
"""
import numpy
from PIL import Image
import numpy as np

cat_image = Image.open("../data/cat_download.jpeg")
array = np.array(cat_image)
print(array.shape)


# 卷积
def numpy_conv(data : np.array, kernel_size=3):
    ones = numpy.ones(kernel_size)
    """
    [1, 2, 3, 4]      [1, 1, 1]
    [4, 5, 6, 4] conv [1, 1, 1] = 
    [7, 8, 9, 4]      [1, 1, 1]
    [1, 2, 3, 4] 
    """
    Hsize = data.shape[0]
    Wsize = data.shape[1]
    print(f"Hsize={Hsize}, Wsize={Wsize}")
    Hsize_out = Hsize - kernel_size + 1
    Wsize_out = Wsize - kernel_size + 1
    print(f"HsizeOut={Hsize_out}, WsizeOut={Wsize_out}")
    zeros_out = np.zeros((Hsize_out, Wsize_out), dtype=np.uint8)
    for i in range(Hsize_out):
        for j in range(Wsize_out):
            sum_v = 0
            for m in range(kernel_size):
                for n in range(kernel_size):
                    sum_v = sum_v + data[i+m][j+n]
            sum_v = sum_v / (kernel_size * kernel_size)
            zeros_out[i][j] = sum_v
    #print(zeros_out)
    return zeros_out

channel1 = array[:, :, 0]
print(channel1.shape)
channel1_after_conv = numpy_conv(channel1, 10)

print("process_channel1")
print(channel1)
data = Image.fromarray(channel1)
data.save("channel1.jpg")

print("process_channel1_after_conv")
print(channel1_after_conv)
data_after_conv = Image.fromarray(channel1_after_conv)
data_after_conv.save("channel1_after_conv.jpg")

# 从结果图片上可以直接看到卷积后的结果