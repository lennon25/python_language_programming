#!/usr/bin/env python3

# Pandas数据的排序

import numpy as np 
import pandas as pd 

# sort_index() 轴索引排序

b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c','a','d','b'])

# 对默认0轴进行排序
b
b.sort_index()
b.sort_index(ascending=False)

# 对1轴排序
c = b.sort_index(axis=1,ascending=False)
c = c.sort_index()

# sort_values() 对轴数值进行排序
a = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
a
c = a.sort_values(2,ascending=False)
c = c.sort_values('b',axis=1,ascending=False)


# Pandas统计分析
# 基本统计分析
a = pd.Series([9,8,7,6],index=['a','b','c','d'])
a
a.sum()
a.count()
a.mean()
a.median()
a.var()
a.max()
a.min()
a.max()
a.describe()

b = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
b.describe()

# 累计统计分析
c = pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','b','d'])
c.cumsum()
c.cumprod()
c.cummax()
c.cummin()


# 相关性分析
# x增大，y增大，两个变量正相关
# x增大，y减小，两个变量负相关
# x增大，y不变，两个变量不相关
# cov()：计算协方差矩阵
# corr()：计算相关系数矩阵，Person、Superman、Kendall等系数
hprice = pd.Series([3.04,22.93,12.75,22.6,12.33], index=['2008','2009','2010','2011','2012'])
m2 = pd.Series([8.18,18.38,9.13,7.82,6.69], index=['2008','2009','2010','2011','2012'])
hprice.corr(m2)




