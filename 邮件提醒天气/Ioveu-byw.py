# -*- coding: utf-8 -*-
import requests
import random
from bs4 import BeautifulSoup
from datetime import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from dateutil.parser import parse
from datetime import datetime
import time
 
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
 
def sendemail(toaddr='946625927@qq.com', message=''):
    fromaddr = 'nqadwrs@163.com' # 你的邮箱
    password = 'ECFSQXJWTKKVJBFI'    # 你的密码
    #此处的密码为163邮箱的smtp密码：https://jingyan.baidu.com/article/c275f6ba33a95de33d7567d9.html
    smtp_server = 'smtp.163.com'     # smtp地址
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = _format_addr('王荣胜 <%s>' % fromaddr)
    msg['To'] = _format_addr('老婆 <%s>' % toaddr)
    msg['Subject'] = Header('来自男朋友王荣胜的问候', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(fromaddr, password)
    server.sendmail(fromaddr, [toaddr], msg.as_string())
    server.quit()
    return
 
def getWeather():
    # 使用BeautifulSoup获取天气信息
    response=requests.get('http://www.weather.com.cn/weather/101120910.shtml')
    #城市代码如果不会查询请讯问我：603329354@qq.com
    response.encoding='uft-8'
    soup=BeautifulSoup(response.text,'html.parser')
    tagToday=soup.find('p', class_="tem")
    try:
        temperatureHigh=tagToday.span.string
    except AttributeError:
        temperatureHigh=tagToday.find_next('p', class_="tem").span.string.replace('℃','')
    temperatureLow=tagToday.i.string.replace('℃','')
    weather=soup.find('p', class_="wea").string
    tagWind=soup.find('p',class_="win")
    winL=tagWind.i.string
    today = datetime.now()
    today = str(today.year)+'年'+str(today.month)+'月'+str(today.day)+'日'
    a = parse('2018-09-30')
    b = datetime.now()
    c= ((b-a).days)
    content = '早安!  我亲爱的白耘玮宝贝~\n'+\
              '今天是:  '+today+'\n'+\
              '沂水温度:  '+temperatureLow+'℃-'+temperatureHigh+'℃\n'+\
              '天气:  '+weather+'\n'+\
              '风级:  '+winL +'\n'+\
              '今天是我们在一起的： ' +str(c) +'天'
    #print(content)
    return content

 
def dailymorning():
    message = getWeather()
    sendemail(toaddr='946625927@qq.com', message=message)
    print("王荣胜，您的媳妇白耘玮已经收到您的天气情况汇报~")
    
if __name__ == '__main__':
    dailymorning()
