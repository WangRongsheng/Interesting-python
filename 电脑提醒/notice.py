from plyer import notification

message='''
你好啊
'''

notification.notify(
        title='疫情提醒',    # 消息标题
        message=message,     # 消息内容
        app_icon='favicon.ico',   # 图标
        timeout=10  # 消息通知时长
        )
