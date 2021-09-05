import os
import random
import time
import cv2
import json
import numpy
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'referer': 'https://www.bilibili.com/'
}


def calcuser(img, user, left, top):
    img.paste(user['upic'], (left, top))
    draw = ImageDraw.Draw(img)
    draw.polygon([(left + 150, top), (left + 600, top), (left + 600, top + 150),
                 (left + 150, top + 150)], fill="#ffffff")
    draw.text((left + 165, top + 5), user['uname'], (0, 0, 0),
              font=ImageFont.truetype("MSYH.TTC", 40, encoding="utf-8"))
    draw.text((left + 165, top + 55), '稿件:%d 粉丝:%d uid:%d LV%d' % (user['videos'], user['fans'], user['uid'], user['level']), (50, 50, 50),
              font=ImageFont.truetype("MSYH.TTC", 20, encoding="utf-8"))
    usign = user['usign']
    if len(usign) > 40:
        usign = usign[0:40] + '...'
    if len(usign) > 20:
        draw.text((left + 165, top + 90), usign[0:20], (50, 50, 50),
                  font=ImageFont.truetype("MSYH.TTC", 20, encoding="utf-8"))
        draw.text((left + 165, top + 110), usign[20:], (50, 50, 50),
                  font=ImageFont.truetype("MSYH.TTC", 20, encoding="utf-8"))
    else:
        draw.text((left + 165, top + 100), usign, (50, 50, 50),
                  font=ImageFont.truetype("MSYH.TTC", 20, encoding="utf-8"))
    return img


def calcusers(img, users):
    if (isinstance(img, numpy.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    i = 0
    for y in range(20, 1080, 180):
        for x in range(20, 1900, 630):
            img = calcuser(img, users[i], x, y)
            i += 1
            if i >= len(users):
                return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


cap = cv2.VideoCapture('video.mp4')
frames = cap.get(7)
fps = cap.get(5)
width = cap.get(3)
height = cap.get(4)
size = (int(width), int(height))
data = json.loads(open('res.json', encoding='utf-8').read())
for p in data:
    s = p['time']
    s = s.split(':')
    p['time'] = int((int(s[0]) * 60 + float(s[1])) * fps)
    for user in p['users']:
        print(user)
        try:
            user['upic'] = Image.open(BytesIO(requests.get(
                url='http:%s@150w_150h_1o.webp' % user['upic'], headers=headers).content))
        except:
            user['upic'] = Image.open(BytesIO(requests.get(
                url='http:%s' % user['upic'], headers=headers).content))
            user['upic'].thumbnail((150, 150))
        if user['usign'] == '':
            user['usign'] = '此用户没有个性签名啊啊啊'
output = cv2.VideoWriter(
    "output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), int(fps), size)
tim = -1
pos = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    tim += 1
    if tim % 100 == 0:
        print(tim)
    if tim < data[pos]['time']:
        output.write(frame)
        continue
    if pos <= len(data) - 2 and tim >= data[pos + 1]['time']:
        pos += 1

    if ret:
        frame = calcusers(frame, data[pos]['users'])
        output.write(frame)
    else:
        break
output.release()
os.system('ffmpeg -i output.mp4 -i video.mp4 -vcodec copy -acodec copy final.mp4')
