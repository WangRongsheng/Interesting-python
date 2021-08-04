import paramiko

# 获取Transport实例
tran = paramiko.Transport(('远程Linux的ip', 22))
# 连接SSH服务端，使用password
tran.connect(username="用户名", password='密码')
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

localpath2 = "./1.txt"
remotepath2 = "/www/wwwroot/1.txt"
# 执行下载动作
sftp.get(remotepath2, localpath2)
# 关闭连接
tran.close()
