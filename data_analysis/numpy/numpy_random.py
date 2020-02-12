
# numpy random随机数函数

import numpy as np

a = np.random.rand(3,4,5)
print(a)

b = np.random.randn(3,4,5)
print(b)

c = np.random.randint(100,200, (3,4))
print(c)

np.random.seed(10)
d = np.random.randint(100,200,(3,4))
print(d)

e = np.random.randint(100,200,(3,4))
print(e)
np.random.shuffle(e)
print(e)
np.random.shuffle(e)
print(e)

f = np.random.randint(100,200, (3,4))
print(f)
print(np.random.permutation(f))
print(np.random.permutation(f))


g = np.random.randint(100,200,(8,))
print(g)
print(np.random.choice(g,(3,2)))
print(np.random.choice(g,(3,2), replace=False))
print(np.random.choice(g,(3,2), p= g/np.sum(g)))

h = np.random.uniform(0,10,(3,4))
print(h)

# # 正态分布
i = np.random.normal(10,5,(3,4))
print(i)



