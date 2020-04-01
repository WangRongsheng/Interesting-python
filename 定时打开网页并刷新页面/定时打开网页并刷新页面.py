# coding = utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()  # 打开火狐浏览器
# driver = webdriver.Chrome()   # 打开Chrome
# driver = webdriver.Ie()   # 打开IE
driver.maximize_window()    #最大化窗口
driver.get('yoursite')    #打开地址
time.sleep(60)    #睡眠60s
driver.refresh()    #刷新打开的页面
driver.close()     #关闭浏览器
