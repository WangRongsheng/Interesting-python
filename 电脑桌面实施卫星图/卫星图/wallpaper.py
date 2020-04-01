# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 19:54:09 2019

@author: wupeng
"""

import requests
import win32api
import win32con
import win32gui
import os
import datetime

def crawlWallpaper(cache_dir='download'):
	if not os.path.exists(cache_dir):
		os.mkdir(cache_dir)
	url_base = 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/'
	date = datetime.datetime.utcnow().strftime('%Y/%m/%d/')
	# 卫星图更新到网站上是有时延的
	hour = str(int(datetime.datetime.utcnow().strftime('%H')) - 1).zfill(2)
	minute = str(datetime.datetime.utcnow().strftime('%M'))[0] + '0'
	second = '00'
	ext = '_0_0.png'
	picture_url = url_base + date + hour + minute + second + ext
	res = requests.get(picture_url)
	with open(os.path.join(cache_dir, 'cache_wallpaper.png'), 'wb') as f:
		f.write(res.content)

def setWallpaper(image_path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,image_path, 1+2)

def main():
	crawlWallpaper('download')
	filepath = os.path.split(os.path.realpath(__file__))[0] + '\download'
	print(filepath)
	image_name='cache_wallpaper.png'
	image_path = filepath + '\\' + image_name
	setWallpaper(image_path)
    
if __name__ == '__main__':
	main()