from urlManager import urlManager
from htmlDownload import htmlDownload
from parseHtml import parseHtml
from dataOutput import dataOutput
from multiprocessing import Pool
from lxml import etree
import json
import time
import os


class spipderMan():
    """
    主逻辑
    """
    def __init__(self):
        """
        初始化各个模块
        """
        self.manager = urlManager()
        self.download = htmlDownload()
        self.parse = parseHtml()
        self.output = dataOutput()

    def get_url(self,n,name):
        """
        获取每一页的 url, 在这里添加多进程进行请求 url
        :return:
        """
        page_urls = self.manager.create_url(n,name)

        p = Pool() # 创建进程池
        for page_url in page_urls:
            #self.request_url(page_url)
            p.apply_async(self.request_url,args=(page_url,)) # #添加进程任务，page_url 为传进去的进程任务的参数
        p.close()  # 不再添加新进程
        p.join()  # 等待所有子进程执行完毕,调用之前必须先调用 close(),针对 Pool 对象

    def request_url(self,page_url):
        """
        请求每一页的 url
        :return:
        """
        response = self.download.request_url(page_url)
        # 判断是否请求成功
        if response == None:
            print('检查网络！！！')
        # 判断是否是最后一页, 就判断是否还有下一页的链接
        html = etree.HTML(response.text)
        if html.xpath('//*[@id="content"]/div/a'):
            self.get_img_url(html,response.text) # response.text 用于正则匹配
        else:
            pass

    def get_img_url(self,html,text):
        """
        解析获取每一页所有图片的 url
        :return:
        """
        img_urls = self.parse.get_this_page_img_urls(html,text)
        self.get_img(img_urls)

    def get_img(self,img_urls):
        """
        下载图片
        :return:
        """
        self.output.download_img(img_urls)


if __name__ == '__main__':
    while True:
        # 打印给用户的提示信息
        print('欢迎使用下载无权图片下载程序~~~\n')
        print('默认下载路径为“D:/无版权图片下载/”\n')
        print('请输入对应的数字下载对应图片（约 1000张）：')
        print('0、默认下载前 1000 张图')
        print('1、自定义下载')
        n = input('请输入序号：')
        if n == '1':
            name = input('\n请输入你想下载的图片类型：')
        if n == '0':
            name = ''
        # 输入错误，重新输入
        if n != '1' and n != '0':
            print('输入错误，重新输入!!!')
            time.sleep(1.5)
            os.system('cls')
            continue
        break
    print('\n------下载开始------')
    print('每条进度条代表 100张（若卡住了可重新运行，下载过了的不会重复下载）')

    try:
        # 运行主接口
        start_time = time.time()
        spider = spipderMan()
        spider.get_url(int(n),name)
        print('\n------下载完成------')
        end_time = time.time()
        print(end_time - start_time)
    except Exception as e: # 打包给用户，如出错显示错误信息
        print(e)
        input()

