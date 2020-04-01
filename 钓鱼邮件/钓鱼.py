import smtplib
import email.mime.text 
 
 
msg = email.mime.text.MIMEText("""
<h2 align="center">奖学金通知</h2>
<p align="center">同学，请速前往
<a href="http://diao-yu-wangzhan.heiheihei">奖学金领取</a>
领取你的奖学金。</p>            
""",'html','utf-8')
 
msg['Subject'] = '奖学金通知' 
msg['From'] = u'XX大学<admin@host.cn>' # 发送方，可以自己编辑
msg['To'] = 'xxx@host.com' # 收件人  
 
 
try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.xx.xx.cn', '25') # smtp服务器链接
    smtp.login('***username***','***password***')
    smtp.sendmail('***username***', 
                  'xxxx@host.com', msg.as_string())
    smtp.quit()
    print('Sucess!')
except Exception as e:
    print(e)
