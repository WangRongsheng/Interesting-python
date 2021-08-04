import paramiko
# ip、用户名、密码
ip = "公网ip"
port = 22
user = "root"
password = "服务器密码"

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()
# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器，地址，端口，用户名密码
ssh.connect(ip, port, user, password, timeout=10)

# 输入linux命令
command = "cd /www/wwwroot ;ls"
stdin, stdout, stderr = ssh.exec_command(command)
# 输出命令执行结果
result = stdout.read()
## bytes 转 str
result = str(result)
result = result.split('\\n')
for i in result:
     print(i)
