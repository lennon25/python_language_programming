#!/usr/bin/env python3
# -*- coding:utf-8 -*-

TempStr = input("请输入带符号的温度值：")

if TempStr[-1] in ["F", "f"]:
	C = (eval(TempStr[0:-1])-32)/1.8
	print("转换后的温度值是: {:.2f}C".format(C))
elif TempStr[-1] in ["C", "c"]:
	F = 1.8*eval(TempStr[0:-1])+ 32
	print("转换后的温度值是: {:.2f}F".format(F))
else:
	print("格式输入错误")