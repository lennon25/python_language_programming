#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import jieba

txt = open("ThreeKingdoms.txt", "r", encoding="GBK").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
	if len(word) == 1:
		continue
	else:
		counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
	word, count = itmes[i]
	print("{0:<10}{1:>5}".format(word,count))
