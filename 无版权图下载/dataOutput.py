import os
import time
from htmlDownload import htmlDownload


class dataOutput():
    """
    数据输出处理
    """
    def __init__(self):
        """
        创建图片保存路径
        """
        self.root_path = r'D:\无版权图片下载\\'
        # 如果没有文件路径就创建
        if not os.path.exists(self.root_path):
            os.mkdir(self.root_path)

        self.download = htmlDownload()

    def download_img(self,img_urls):
        """
        下载图片的函数
        :param img_urls: 图片名称，url 对应的列表
        :return:
        """
        count = 0 # 进度条计数
        for url in img_urls:
            # 构造图片的完整下载路线
            download_path = '{}{}'.format(self.root_path,url[58:])
            if not os.path.exists(download_path):
                response = self.download.request_url(url)
                try:
                    with open(download_path, 'wb') as f:
                        f.write(response.content)
                except:
                    pass
            else:
                pass

            count += 1
            self.progress_bar(count,len(img_urls))

    def progress_bar(self,count,lenth):
        """
        显示进度条
        :return:
        """
        a = '*' * count
        b = '.' * (lenth - count)
        c = (count / lenth) * 100
        print('\r{:^2.0f}%[{}->{}]'.format(c, a, b), end='')
        time.sleep(0.1)







