#!/usr/bin/env python3

import requests


def getHTMLText(url):
	try:
		r = requests.get(url, timemout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		print(r.text)
		return r.text
	except:
		return "request error"


if '__name__' == '__main__':
	url = "http://www.baidu.com"
	print(getHTMLText(url))
# r = requests.get("http://www.baidu.com")
# r.raise_for_status
# r.encoding=r.apparent_encoding
# print(r.text)