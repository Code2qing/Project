#-*- coding:utf-8 -*-
#!/usr/bin/env python
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import time

url="http://cs.58.com/pinpaigongyu/pn/{page}/?minprice={minrent}_{maxrent}"

minrent=input("请输入最低租金")
maxrent=input("请输入最高租金")
page = 0

csv_file = open("rent.csv","w")
csv_writer = csv.writer(csv_file,delimiter=',')

while True:
	page += 1
	if page%25 == 0:
		print("暂停一下....")
		time.sleep(6)
	print("fetch:",url.format(page=page,minrent=minrent,maxrent=maxrent))
	response=requests.get(url.format(page=page,minrent=minrent,maxrent=maxrent))
	text=str(response.text)
	html = BeautifulSoup(text,"html.parser")
	house_list = html.select(".list > li") #CSS选择器 --https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

	if not house_list:
		break

	for house in house_list:
		house_title = str(house.select("h2")[0]).replace('<h2>','')
		house_title = house_title.replace('</h2>','')
		house_url = urljoin(url,house.select("a")[0]["href"])
		house_info_list = str(house_title).split()
		#切片

		#以标题第三列为地址
		house_location = house_info_list[1]


		house_money = str(house.select(".money > span > b")[0]).replace('<b>','')
		house_money = house_money.replace('</b>','')
		#将当前房源逐行写入csv文件
		csv_writer.writerow([house_title,house_location,house_money,house_url])

csv_file.close()
