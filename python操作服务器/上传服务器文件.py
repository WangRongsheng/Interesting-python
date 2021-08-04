import paramiko

# 获取Transport实例
tran = paramiko.Transport(('远程Linux的ip', 22))
# 连接SSH服务端，使用password
tran.connect(username="用户名", password='密码')
# 获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

# 设置上传的本地/远程文件路径
localpath = "./1.txt"
remotepath = "/www/wwwroot/1.txt"

# 执行上传动作
sftp.put(localpath, remotepath)
# 关闭连接
tran.close()
