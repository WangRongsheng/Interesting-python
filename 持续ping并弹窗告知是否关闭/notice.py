#coding=utf-8

import os
import time
count = 3   #最大检测次数，即第一次检测不存在则安装，会有安装失败的情况，就会再来一次
while count:
    try:
        from plyer import notification
        print ('plyer模块已安装')
        break
    except:
        print ('plyer模块未安装,现在准备开始安装')
        os.system('pip install plyer')
        count -= 1
        continue

num = 0
while(1):
    num = num +1
    message = []
    command = 'ping 122.206.78.18' #可以直接在命令行中执行的命令
    r = os.popen(command) #执行该命令
    info = r.readlines() #读取命令行的输出到一个list
    for line in info: #按行遍历
        message.append(line)
        # line = line.strip('\r')
    # print(message[2])
    if message[2]=='请求超时。\n':
        notification.notify(
            title='连接提醒',    # 消息标题
            message='ping不通，连接断开！请联系管理员处理！',  # 消息内容
            app_icon='favicon.ico',   # 图标
            timeout=10  # 消息通知时长
            )
        break
    time.sleep(120)
    message.clear()
    print('已经执行ping了{}次！'.format(num))
