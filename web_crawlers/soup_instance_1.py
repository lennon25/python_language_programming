#!/usr/bin/env python3

"""中国大学排名网站定向爬虫（针对url定向爬取）"""

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return " "

def fullUnivList(ulist,html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find("tbody").children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}\t"
	print(tplt.format("排名","学校名称","总分", chr(12288)))
	for i in range(num):
		u = ulist[i]
		# print(u)
		print(tplt.format(u[0],u[1], u[2], chr(12288)))

def main():
	uinfo = []
	url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
	html = getHTMLText(url)
	fullUnivList(uinfo, html)
	printUnivList(uinfo, 20) # 20 univs

main()
