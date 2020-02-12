
import pandas as pd
import numpy as np

# DataFrame类型： 行列索引+二维数组，由共用相同索引的一组列组成（索引+多列数据）

# DataFrame创建：二维ndarray，一维ndarray，列表，字典，元组，Series类型，其他DataFrame类型

# 二维数组创建
d = pd.DataFrame(np.arange(10).reshape(2,5))
d

# 一维ndarray的字典创建：
dt = {'one': pd.Series([1,2,3],index=['a','b','c']),
	'two': pd.Series([9,8,7,6],index=['a','b','c','d'])}
d= pd.DataFrame(dt)
d
pd.DataFrame(dt,index=['b','c','d'],columns=['one','two','three'])

# 列表类型的字典创建
dl = {"one": [1,2,3,4],"two":[9,8,7,6]}
# d = pd.DataFrame(dl)
d = pd.DataFrame(dl,index = ["a","b","c","d"])
print(d)


dl = {"城市":["北京","上海","广州","深圳","沈阳"],
	"环比": [101.5,101.2,101.3,102.0,100.1],
	"同比": [120.3,127.3,119.4,130.9,101.4],
	"定基": [121.4,127.8,120.0,145.5,101.6]}

d = pd.DataFrame(dl,index=["c1","c2","c3","c4","c5"])


# 重新索引
d = d.reindex(index=['c5','c4','c3','c2','c1'])
d = d.reindex(columns=['城市','同比','环比','定基']

# 增加
newc = d.columns.insert(4,'新增')
newd = d.reindex(columns=newc,fill_value=200)
newd

nc = d.columns.delete(2)
ni= d.index.insert(5,'c1')
nd = d.reindex(index=ni,columns=nc,method='ffill')


# 删除
d.drop('c5')
d.drop('同比',axis=1)


# 算术运算规则
# 根据行列进行索引，补齐后运算，默认生成浮点数，缺省补NaN，不同维度之间运算时为广播运算

a = pd.DataFrame(np.arange(12).reshape(3,4))
b = pd.DataFrame(np.arange(20).reshape(4,5))
a + b
a * b

# 算术函数
b.add(a,fill_value=10)
a.mul(b,fill_value=0)

# 不同维度运算
c = pd.Series(np.arange(4))
c + 10
b + c


# 比较运算：（只能比较相同索引的元素，不进行补齐，不同维度为广播运算，二元运算产生布尔对象）

# 同维度比较运算
a = pd.DataFrame(np.arange(12).reshape(3,4))
b = pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
a > b
a == b

# 不同维度比较运算
a = pd.DataFrame(np.arange(12).reshape(3,4))
c = pd.Series(np.arange(4))
a > c
c > 0






