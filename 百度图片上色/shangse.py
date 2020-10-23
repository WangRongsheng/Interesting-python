import base64
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=你的AK&client_secret=你的SK'
response = requests.get(host)
if response:
    print(response.json())

# 黑白图像上色
request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/colourize"
# 二进制方式打开图片文件
f = open('test.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = response.json()['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())

# base64编码转图片
img = base64.b64decode(response.json()['image'])
file = open('result.jpg', 'wb')
file.write(img)
file.close()
