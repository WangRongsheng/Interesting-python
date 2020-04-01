# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup as bs


class Riddles(object):
	def __init__(self):
		self.df = pd.DataFrame(columns=['谜面', '谜底','提示'])

	def get_list(self, url):
		r = requests.get(url)
		self.parse_list(r.text)

	def parse_list(self, html):
		s = etree.HTML(html)
		items = s.xpath('/html/body/div[6]/div[1]/div/div[2]/ul/li')
		for item in items:
			detUrl = r'http://www.cmiyu.com' + item.xpath('a/@href')[0]
			self.get_detail(detUrl)
		self.save_data()

	def get_detail(self, url):
		print(url)
		r = requests.get(url)
		r.encoding = 'gb2312'
		soup = bs(r.text, 'lxml')
		prompt = soup.find('div', class_='zy').text
		h3s = soup.find('div', class_='md').find_all('h3')
		ques = h3s[0].text
		ans = h3s[1].text
		self.df = self.df.append(pd.DataFrame.from_dict({'谜面': ques, '谜底': ans, '提示': prompt}, orient='index').T,
								 ignore_index=True)

	def save_data(self):
		self.df.to_csv('new_data1.csv', index=False, mode='a')
		self.df = pd.DataFrame(columns=['谜面', '谜底', '提示'])



if __name__ == '__main__':
	riddles = Riddles()
	for i in range(20, 151):
		print('page', str(i))
		url = r'http://www.cmiyu.com/dmmy/my18' + str(i) + '.html'
		print(url)
		riddles.get_list(url)
