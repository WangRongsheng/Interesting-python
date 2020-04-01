import os
import shutil
import sqlite3
import win32crypt

db_file_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Login Data')

tmp_file = os.path.join(os.environ['LOCALAPPDATA'], 'sqlite_file')
print(tmp_file)
if os.path.exists(tmp_file):
    os.remove(tmp_file)
shutil.copyfile(db_file_path, tmp_file)

conn = sqlite3.connect(tmp_file)
for row in conn.execute('select signon_realm,username_value,password_value from logins'):
    ret = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)
    print('网站：%-50s，用户名：%-20s，密码：%s' % (row[0][:50], row[1], ret[1].decode('gbk')))

conn.close()
os.remove(tmp_file)
