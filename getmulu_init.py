import requests
from bs4 import BeautifulSoup

url = 'http://seputu.com/'
ht = requests.get(url)
ht.encoding = ht.apparent_encoding
hts = BeautifulSoup(ht.text, 'html.parser')

for par in range(9):  # 做一个计数，只输出8个
	part = hts.find_all(class_='mulu')[par]
	if part.find('h2'):
		print('\n' + part.h2.string + '\n')
		# 此处输出大标题
		for i in part.find_all(class_='box'):
			for p in i.ul.contents:
				if p.string:
					print(p.string)  # 章节题目
					if p.name:
						print(p.a.get('href'))  # 章节的链接
					# 获取每个章节的题目
					# 以及每个章节的链接
