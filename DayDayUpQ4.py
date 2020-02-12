#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def dayUp(dayfactor):
	dayup = 1.0
	for i in range(365):
		if i % 7 in [6, 0]:
			dayup *= 1 - 0.01
		else:
			dayup *= 1 + dayfactor
	return dayup


df = 0.01
while dayUp(df) < 37.78:
	df += 0.001
print("工作日需努力倍数: {:.3f}".format(df))
