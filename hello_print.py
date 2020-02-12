#!/usr/bin/env python3
# -*- coding:utf-8 -*-

p = eval(input("Please input a int:"))

if p == 0:
	print("Hello World")
elif p > 0:
	print("He\nll\no \nWo\nrl\nd")
else:
	for i in "Hello World":
		print(i)