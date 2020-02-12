
# numpy 统计函数

import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
print(np.sum(a))

print(np.mean(a, axis=1))

print(np.average(a, axis=0, weights=[10,5,1]))

print(np.std(a))

print(np.var(a))


# 其他的统计函数
b = np.arange(15,0,-1).reshape(3,5)
print(b)
print(np.min(b))
print(np.max(b))
print(np.argmin(b))
print(np.argmax(b))
print(np.argmax(b),b.shape)
print(np.ptp(b))
print(np.median(b))


# numpy中的梯度函数
c = np.random.randint(0,20,(5))
print(c)
print(np.gradient(c))

d = np.random.randint(0,50,(3,5))
print(d)
print(np.gradient(d))


