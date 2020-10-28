import paramiko
import sys


def process_bar(now, total):
    """进度条"""
    process = int(now * 100 / total)
    sys.stdout.write(f"\r[ {process}% ]" + ">" * process)
    sys.stdout.flush()
    

trans = paramiko.Transport(("公网ip", 22))
trans.connect(username="root", password="服务器密码")
# 秘钥
# private = paramiko.RSAKey.from_private_key_file()  
# trans = paramiko.Transport(("123.206.16.61", 22))
# trans.connect(username="root", pkey=private)

# ssh通信
ssh = paramiko.SSHClient()
ssh._transport = trans  # 绑定连接
# 执行shell命令
stdin, stdout, stderr = ssh.exec_command("ls -l")
print(stdout.read().decode("utf-8"))
print(stderr.read().decode("utf-8"))

# ftp
ftp = trans.open_sftp_client()
# 上传文件
ftp.put("0.830.pth", "0.830.pth", callback=process_bar)
# 下载文件
# ftp.get("flower.jpg", "flower_new.jpg", callback=process_bar)