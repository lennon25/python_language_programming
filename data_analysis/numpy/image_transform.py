
from PIL import Image
import numpy as np

# 读取image 表示为数组
a = np.array(Image.open("timg1.jpeg").convert("L"))

print(a.shape, a.dtype)

# b = [255,255,255] - a
# b = 255 - a
b = (100/255)*a + 150


im = Image.fromarray(b.astype("uint8"))

im.save("timg_3.jpeg")