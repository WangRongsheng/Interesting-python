if __name__=="__main__":
    print("很抱歉，这个是一个模块，请不要运行它。")
else:
    from requests import get
    from bs4 import BeautifulSoup
    from json import loads
class api:
    def __init__(self):
        content=get("https://3g.dxy.cn/newh5/view/pneumonia")
        content.encoding='utf-8'
        data=content.text
        self.bs = BeautifulSoup(data,'html.parser')
    def guonei(self):
        a=self.bs.find(id="getAreaStat").prettify()
        b=a.replace('<script id="getAreaStat">','')
        a=b.replace('</script>','')
        b=a.replace('}catch(e){}','')
        a=b.replace(' try { window.getAreaStat = ','')
        return loads(a)
    def guowai(self):
        a=self.bs.find(id="getListByCountryTypeService2").prettify()
        b=a.replace('<script id="getListByCountryTypeService2">','')
        a=b.replace('</script>','')
        b=a.replace('}catch(e){}','')
        a=b.replace(' try { window.getListByCountryTypeService2 = ','')
        return loads(a)
    def data(self):
        a=self.bs.find(id="getStatisticsService").prettify()
        b=a.replace('<script id="getStatisticsService">','')
        a=b.replace('</script>','')
        b=a.replace('}catch(e){}','')
        a=b.replace(' try { window.getStatisticsService = ','')
        return loads(a)