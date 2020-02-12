#!/usr/bin/env python3

import numpy as np

# # 存储csv文件
# a = np.arange(100).reshape(5,20)
# # np.savetxt('a.csv', a,fmt="%d",delimiter=",")
# np.savetxt("a.csv", a, fmt="%.1f", delimiter=",")

# # 读取csv文件
# b = np.loadtxt("a.csv",dtype=np.int32, delimiter=",")
# print(b)


# 存取任意维度的数据
a = np.arange(100).reshape(5,10,2)
a.tofile("b.dat", sep=",", format="%d")

# 存入文本文件
b = np.fromfile("b.dat", dtype=np.int, sep=",")
b = np.fromfile("b.dat", dtype=np.int, sep=",").reshape(5,10,2)
print(b)

# 存入二进制文件
a.tofile("c.dat", format="%d")
c = np.fromfile("c.dat",dtype=np.int).reshape(5,10,2)
print(c)


# Numpy文件读取方法，np.save, np.load
x = np.arange(100).reshape(5,10,2)

np.save("d.npy",a)
d = np.load("d.npy")
print(d)







