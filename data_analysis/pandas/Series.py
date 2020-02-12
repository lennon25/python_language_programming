import pandas as pd 
import numpy as np


# Pandas中的核心数据类型： Series，DataFrame

# Series类型： 一组数据及与之相关的数据索引组成

a = pd.Series([9,8,7,6])
a

b = pd.Series([9,8,7,6],index=['a','b','c','d'])
b

c = pd.Series(25, index=['a','b','c'])
c

a = pd.Series({"a":1,"b":2,"c":3,"d":4})
print(a)
print(a[1])
print(a["b"])



d = pd.Series(range(20))
print(d)
d.cumsum()

e = pd.Series(np.arange(5))
e

n = pd.Series(np.arange(5),index=np.arnge(9,4,-1))
n


k = pd.Series([1,2,3],['c','d','e'])
v = pd.Series([9,8,7,6],['a','b','c','d'])
k + v

v = pd.Series([9,8,7,6],['a','b','c','d'])
v['b']= 15
v.name="Series"
v['a','c'] = 20



