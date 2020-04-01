import re


class parseHtml():
    """
    解析网页，提取数据
    """
    def __init__(self):
        self.img_urls = [] # 存储图片标题和 url 的列表

    def get_this_page_img_urls(self,html,text):
        """
        获取此页图片的 url
        :param html:
        :return: 存储图片 url 的列表
        """
        # 打印当前下载了多少图片，先判断是否访问成功，成功就打印
        img_urls = re.findall('srcset="(.*?)"',text,re.S)
        for img_url in img_urls:
            img_url = img_url.split(' 1x, ')[0]
            self.img_urls.append(img_url)
        return self.img_urls

