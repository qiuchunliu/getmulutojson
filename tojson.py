import json

with open('qqq.json', 'r', encoding='utf-8') as f:
# 注意 encoding = 'utf-8'
	ff = json.load(f)
	# 通常的文件读取
for i in ff:
# for 循环读取内容
	print(i)
