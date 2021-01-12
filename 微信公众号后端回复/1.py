# coding:utf-8
# 被关注回复
# 收到 笑话 回复糗百笑话，收到收到 电影 回复电影天堂最新电影，
# 收到 blog 回复我的简书博客，收到 音乐 回复一首音乐
# 收到 fight 回复一句话
 
from werobot import WeRoBot
import random
from werobot.replies import ArticlesReply, Article
 
robot = WeRoBot(token='。。。')
 
 
# 明文模式不需要下面三项
# robot.config["APP_ID"]=''
# robot.config["APP_SECRET"]=''
# robot.config['ENCODING_AES_KEY'] = ''
 
# 被关注
@robot.subscribe
def subscribe(message):
    return '''咕噜咕噜~联系王荣胜的私密通道为你开启~
'''
 
 
# 读取文档里的笑话，把前三行存在 data2 里，字符串太长公众号会报错
def joke_data():
    filename = 'qiushibaike.txt'
    f = open(filename, 'r')
    data = f.read()
    f.close()
    data1 = data.split()
    data2 = ''
    for data_i in data1[0:3]:
        data2 += data_i + '\n' + '\n'
    return data2
 
 
# 读取文档里的电影名称
def movie_name():
    filename = 'movies_name.txt'
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data
 
 
# 从三首音乐里随机选一首
def music_data():
    music_list = [
        ['童话镇', '陈一发儿', 'https://e.coka.la/wlae62.mp3', 'https://e.coka.la/wlae62.mp3'],
        ['都选C', '缝纫机乐队', 'https://files.catbox.moe/duefwe.mp3', 'https://files.catbox.moe/duefwe.mp3'],
        ['精彩才刚刚开始', '易烊千玺', 'https://e.coka.la/PdqQMY.mp3', 'https://e.coka.la/PdqQMY.mp3']
    ]
    num = random.randint(0, 2)
    return music_list[num]
 
 
# 读取 fight.txt 里的句子，随机返回一句
def get_fighttxt():
    filename = 'fight.txt'
    f = open(filename, 'r')
    data = f.read()
    f.close()
    data1 = data.split()
    max_num = len(data1) - 1
    num = random.randint(0, max_num)
    data2 = data1[num]
    return data2
 
 
# 匹配 笑话 回复糗百笑话
@robot.filter('笑话')
def joke(message):
    data = joke_data()
    return data
 
 
# 如果用
# @robot.text
# def joke(message):
#    if message.content == "笑话":
# 会报错
# UnicodeWarning: Unicode equal comparison failed to 
# convert both arguments to Unicode - interpreting them as being unequal
 
# 匹配 电影 回复电影名称
@robot.filter('电影')
def movie(message):
    name = movie_name()
    return name
 
 
# blog 回复个人博客
@robot.filter('blog')
def blog(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="v1coder",
        description="我的个人博客",
        img="https://upload.jianshu.io/users/upload_avatars/9691564/d4404291-308a-4159-b324-4ae400d8c977.png",
        url="https://www.jianshu.com/u/7cb04d09491e"
    )
    reply.add_article(article)
    return reply
 
 
# 匹配 音乐 回复一首歌
@robot.filter('音乐')
def music(message):
    music1 = music_data()
    return music1
 
 
# 匹配 fight 回复一句话
@robot.filter('fight')
def fight(message):
    data = get_fighttxt()
    return data
 
 
# 文本消息返回原文
@robot.text
def echo(message):
    return message.content
 
 
# 其他消息返回
@robot.handler
def hello(message):
    return '(O_o)??'
 
 
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
