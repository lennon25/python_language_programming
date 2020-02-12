#!/sur/bin/env python3
import requests, os


url = "https://www.nationalgeographic.com/content/dam/expeditions/destinations/africa/family-journeys/morocco/hero-morocco-fam-journey.adapt.1900.1.jpg"
root = "./"
path = root + url.split("/")[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		r.raise_for_status()
		with open(path, "wb") as f:
			f.write(r.content)
			f.close()
		print("文件保存成功")
	else:
		print("文件已经存在")
except:
	print("爬取失败")