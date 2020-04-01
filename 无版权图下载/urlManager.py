class urlManager():
    """
    管理 url
    """
    def __init__(self):
        """
        初始化需要拼接的 url
        """
        self.base_url = 'https://pixabay.com/zh/images/search/{}?pagi={}'

    def create_url(self,n,name=''):
        """
        构造每一页的 url
        :return:
        """
        if n == 0:
            urls = [self.base_url.format('',str(i)) for i in range(1,11)]
        elif n == 1:
            urls = [self.base_url.format(name + '/',str(i)) for i in range(1,11)]
        return urls
