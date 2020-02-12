#!/usr/bin/env python3

# Numpy是开源的python第三方的科学计算基础库

import numpy as np

a = np.array([0,1,2,3,4])
b = np.array([9,8,7,6,5])

c = a**2 + b**3

print(c)

# 创建ndarray数组
x = np.array([4,5,6,7])
print(x)
x = np.array([[1,2],[8,9],(0.1,0.2)])
print(x)

x = np.arange(10)
print(x)

x = np.ones((3,6))
print(x)

x = np.zeros((3,6),dtype=np.int32)
print(x)

x = np.eye(5)
print(x)

x =np.linspace(1,10,4)
print(x)


# 数组的索引和切片
a = np.array([9,8,7,6,5])
print(a[2])
print(a[1:4:2])

a = np.arange(24).reshape(2,3,4)

# 索引
print(a[1,2,3])
print(a[0,1,2])
print(a[-1,-2,-3])

# 切片
print(a[:,1,-3])
print(a[:,1:3,:])
print(a[:,:,::2])




