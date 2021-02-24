import requests
import pyttsx3
from lxml import etree
 
url = 'https://www.tianqi.com/beijing/'
headers = {'content-type':'application/json', 'User-Agent':'Mozilla/5.0 (Xll; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 
# 向目标url地址发送请求，返回一个response对象
req = requests.get(url=url, headers=headers)
# .text是response对象的网页html
html = req.text
html_obj = etree.HTML(html)
html_data = html_obj.xpath("//dl[@class='weather_info']//text()")
 
word = "欢迎使用天气播报助手"
 
for data in html_data:
    word += data
 
word = word.replace('[切换城市]','')
word += '\n播报完毕！谢谢！'
print(word)
 
ptt = pyttsx3.init()
ptt.say(word)
ptt.runAndWait()