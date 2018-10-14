import requests
from bs4 import BeautifulSoup
import json

url = 'http://seputu.com/'
ht = requests.get(url)
ht.encoding = ht.apparent_encoding
hts = BeautifulSoup(ht.text, 'html.parser')

content = []
for par in range(9):  # 做一个计数，只输出8个
	part = hts.find_all(class_='mulu')[par]
	if part.find('h2'):
		h2title = part.h2.string
		listt = []
		for i in part.find_all(class_='box'):
			for p in i.ul.contents:
				if p.string:
					box_title = p.string  # 章节题目
					if p.name:
						href = p.a.get('href')  # 章节的链接
					# 获取每个章节的题目
					# 以及每个章节的链接
						listt.append({'href': href, 'box_title': box_title})
		content.append({'title': h2title, 'content': listt})
with open('qqq.json', 'w') as fp:
	json.dump(content, fp=fp, indent=4)
