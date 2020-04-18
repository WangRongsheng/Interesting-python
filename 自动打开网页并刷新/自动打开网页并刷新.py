from time import sleep
from selenium import webdriver

driver= webdriver.Firefox() #  需要下载对应浏览器驱动到 python 安装目录
driver.get("https://storeweb.cn/") # 刷新网址

for i in range(10000): # 刷新次数
    driver.refresh()  # 刷新网页
    sleep(60) # 五秒一次
