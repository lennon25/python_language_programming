
import pandas as pd 


dl = {"城市":["北京","上海","广州","深圳","沈阳"],
	"环比": [101.5,101.2,101.3,102.0,100.1],
	"同比": [120.3,127.3,119.4,130.9,101.4],
	"定基": [121.4,127.8,120.0,145.5,101.6]}

d = pd.DataFrame(dl,index=["c1","c2","c3","c4","c5"])
print(d)
print(d.index)
print(d.columns)
print(d.values)
print(d["同比"])
print(d.ix["c2"])
print(d["同比"]["c2"])

