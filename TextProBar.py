#!/usr/bin/env python3

import time

# scale = 10
# print("----------Start----------")
# for i in range(scale + 1):
# 	a = '*' * i
# 	b = '.' * (scale - i)
# 	c = i * 10
# 	print("{:^3.0f}%[{}->{}]".format(c,a,b))
# 	time.sleep(0.1)
# print("----------End----------")


# 单行动态刷新
# for i in range(101):
# 	print("\r当前进度值:{:3}%".format(i),end=" ")
# 	time.sleep(0.1)


# ***完整进度效果***  
scale = 50
print("Start".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
	a = "*" * i
	b = "." * (scale - i)
	c = i /scale * 100
	dur = time.perf_counter() -start
	print("\r{0:3.0f}%[{1}->{2}]{3:.2f}s".format(c,a,b,dur), end="")
	time.sleep(0.1)
print("\n"+ "End".center(scale//2,"-"))