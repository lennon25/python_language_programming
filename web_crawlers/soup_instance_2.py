#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup


"""天猫商城产品比价爬取"""

def getHTMLText(url):
	try:
		r = requests.get(url, timeout= 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt, html):
	soup = BeautifulSoup(html, "html.parser")
	prds = soup.find_all("div", attrs={"class":"product-iWrap"})
	try:
		for i in prds:
			price = i.em["title"]
			product = i.find("div", attrs={"class": "productTitle productTitle-spu"}).a["title"]
			ilt.append([price,product])
	except:
		print("")

def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}\t"
	print(tplt.format("序号", "价格", "名称"))
	count = 0
	for i in ilt:
		count += 1
		print(tplt.format(count, i[0],i[1]))
	print("")

def main():
	goods = "Macbook"
	url = "https://list.tmall.com/search_product.htm?q=" + goods
	infoList = []
	try:
		html =getHTMLText(url)
		parsePage(infoList, html)
	except:
		print("")
	printGoodsList(infoList)


if __name__ == "__main__":
	main()


