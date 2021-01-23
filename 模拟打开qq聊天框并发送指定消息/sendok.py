# coding = utf-8
import time
import win32gui
import win32con
import win32clipboard
import os

class CSendQQMsg():
    def __init__(self, friendName, msg):
        self.friendName = friendName
        self.msg=msg

    def setText(self):#把要发送的消息复制到剪贴板
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        win32clipboard.CloseClipboard()

    def sendmsg(self):#给好友发送消息
        self.setText()
        hwndQQ = win32gui.FindWindow(None,self.friendName)#找到名字为'四'的窗口
        if hwndQQ == 0:
            print('未找到qq对话框')
            return
        win32gui.SendMessage(hwndQQ,win32con.WM_PASTE , 0, 0)
        win32gui.SendMessage(hwndQQ, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


if __name__ == '__main__':
    # 打开聊天框
    os.system(r'E:\"sougou"\"SogouExplorer"\SogouExplorer.exe https://qm.qq.com/cgi-bin/qm/qr?k=0NRHg9fJIKPmiX4kT6Gp7htFu6jeW_UW&jump_from=webapi')
    time.sleep(5)
    os.system('taskkill /F /IM SogouExplorer.exe')
    time.sleep(5)
    
    # 当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    # 进行自动提交
    friendName='四'
    msg="今日已打卡" + '\n' + '打卡时间为：'+now_time
    qq = CSendQQMsg(friendName,msg)
    qq.sendmsg()
