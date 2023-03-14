#!/usr/bin/env python3

# 递归的基本结构： 函数 + 分支语句， 递归分为递归链条和递归基例

# 字符串递归反转
def rvs(s):
	if s == "":
		return s
	else:
		return rvs(s[1:]) + s[0]


# 斐波那契数列
def feb(n):
	if n == 1 or n == 2:
		return 1
	else:
		return feb(n - 1) + feb(n - 2)


# 汉罗塔
count = 0
def hanoi(n, src, dst, mid):
	global count 
	if n == 1:
		print("{}:{}->{}".format(1, src, dst))
		count += 1
	else:
		hanoi(n-1, src, mid, dst)
		print("{}:{}->{}".format(n,src,dst))
		count += 1
	hanoi(n-1, mid, dst, src)