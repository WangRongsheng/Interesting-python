from bs4 import BeautifulSoup  # 靓汤 解析网页获取数据
import re  # 正则处理
import urllib.request, urllib.error  # 指定url获取网页数据
import pymysql
import xlwt


def main():
    baseurl = "https://movie.douban.com/top250?start="
    dataList = getData(baseurl)
    savePath = '豆瓣电影TOP250.xls'
    saveData(dataList, savePath)
    saveData2DB(dataList, "moviedb")
    # askUrl(baseurl)
#========================正则定义===========================
# r''  r忽视特殊符号  '' 防止网站中的双引号冲突
# <a href="https://movie.douban.com/subject/3442220/">
# 我们查看内容中 有一个开头 <a href=" 为开头  中间很多内容
# .一个字符 用一个元组装起来  .*? 某个字符 出现很多次
# 最后结尾部分 "> 结尾
findlink = re.compile(r'<a href="(.*?)">') # 创建正则表达对象 正则规则 帮助我们快速锁定链接
# 为了方便看到item 我们在下面打印一下
# print(item)

# <img alt = "肖申克的救赎"class =""src = "https://img3.doubanio.com/view
# /photo/s_ratio_poster/public/p480747492.jpg"width = "100" / >
# <img开头 后面若干个字符 .* src=  很多字符出现(.*?) 最终结束以"结束
# 可能截取到的内容存在换行情况 所以加上规则 re.S 忽略换行继续往后匹配
# 影片图片的规则
findImageSrc = re.compile(r'<img.*src="(.*?)"',re.S)
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 找到评价人数 <span>2062397人评价</span>   数字  人评价
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到介绍 <span class="inq">希望让人自由。</span>
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
# 所有内容都找到,我们下去匹配内容

#===================================================
# 下面已经有了一个网页内容的获取  我们每个页面25部电影 需要调用 10 次
# 我们不可能写十次代码,但是我们可以使用循环机制
def getData(baseurl):
    dataList = []
    for i in range(0, 10):  # 含头不含尾  也就是 0123456789 分别*25 调用十次函数 拼接十个地址
        url = baseurl + str(i * 25)  # 也就是我们从start = 0 (0-25) # start = 25 50 网页一个一个输入一下网址看效果
        html = askUrl(url)  # 调用函数返回html
        # print(html)
        # 接下来逐一解析网页 因为一个网页需要解析一次 所以我们还是写在for循环里面
        # *****testBeautifulSoup*************解析网页*************自动化办公之批量新增excel图片*****新建****
        # 接下来进行解析过程   需要一个靓汤
        soup = BeautifulSoup(html,"html.parser")
        # 打开网页 我们会发现 整个豆瓣里面所有的内容都在一个class = "item"里面
        # 我们右键 edit as html 就可以随意复制
        # 括号参数:寻找所有div并且class为item的标签
        for item in soup.find_all("div", class_="item"): # 查找符合要求的字符串 形成列表
            # print(item) # 测试查看电影item
            # 现在我们发现已经拿到具体的内容了,现在要把一个电影里面的内容一个一个存储起来
            data = []   # 保存一部电影的重要信息
            item = str(item)    # 转换成 字符串 正则转换
            #===============后续查找
            # print(item)
            #===============后续结束

            # 正则定义成全局变量 主方法下面 方法上面
            # 0 为了防止一个标签下多个电影名称
            link = re.findall(findlink,item)[0] # re库用来通过正则查找指定字符串
            data.append(link)
            imSrc = re.findall(findImageSrc,item)[0]

            print(item)
            print(imSrc)

            data.append(imSrc)
            # title这里要注意 有中文名,英文名,需要对应匹配
            titles = re.findall(findTitle,item)
            if len(titles) == 2:
                data.append(titles[0])
                data.append(titles[1].replace("/", "")) # 把英文名字存进去 替换掉前面的/
            else:   # 否则 添加中文名称    英文名称留空  为了保持一致性 进数据库方便
                data.append(titles[0])
                data.append(" ") # 英文名称留空
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judge = re.findall(findJudge,item)[0]
            data.append(judge)
            # 实际添加过程中 inq可能没有 所以这里需要加判断
            inq = re.findall(findInq,item)
            if len(inq)!=0:
                data.append(inq[0].replace("。",""))
            else:
                data.append(" ") #否则添加一个空的

# 导演: 克里斯托弗·诺兰 Christopher Nolan   主演: 克里斯蒂安·贝尔 Christ...<br/>
# 2008 / 美国 英国 / 剧情 动作 科幻 犯罪 惊悚
            # bd中有一个 <br/> / 去掉
            bd = re.findall(findBd,item)[0]
            # br / 中间可能有空白符(\s匹配空白符) 一个或多个 都匹配
            bd = re.sub('<br(\s+)?/>(\s+)?', " ",bd)  # 替换内容 对 bd操作
            bd = re.sub('/', " " ,bd)    # 去掉/
            data.append(bd.strip()) # 去掉空格

            dataList.append(data)   # 处理好的电影信息放进list

    # print(dataList)
    return dataList

# 得到一个指定url的网页内容
def askUrl(url):
    # 用户代理 表示告诉豆瓣服务器我们的浏览器信息(本质上是告诉服务器,我们能接收什么数据)
    head = {  # 模拟豆瓣向豆瓣服务器发送
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.116 Safari/537.36"}
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    #     可能会出现的错误信息 urlerror 404 500
    except urllib.error.URLError as e:
        # 如果出现错误 我们拿到报错信息中的code
        if hasattr(e, "code"):
            print(e.code)
    return html

# 保存数据
def saveData(datalist, savePath):
    workbook = xlwt.Workbook(encoding='UTF-8',style_compression=0)  # 1创建工作簿 数据不压缩
    worksheet = workbook.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)  # 2创建工作表  可以被覆盖

    col = ("电影详情链接","图片链接","影片中文名称","外国名称","评分","评价人数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
# 保存数据
    workbook.save(savePath)

# 数据库存储数据
def saveData2DB(dataList, savePath):
    print("数据库存储")
    init_db()
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", savePath)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cur = db.cursor()
    # dataList 是一条一条的信息,我们需要把所有信息存储到数据库
    for data in dataList:
        for index in range(len(data)):
            # 拿出每一个字符串 加引号 放回去
            data[index] = '"'+data[index]+'"'
            # 每拼好一个语句就执行一次sql
        sql = '''
        INSERT INTO movie250(
        info_link,pic_link,cname,ename,score,rated,instroduction,info)
        VALUES (%s)
        '''%",".join(data)
        print(sql)
        cur.execute(sql)
    db.commit()
    db.close()


def init_db():
    sqlCheck = "DROP TABLE IF EXISTS movie250;"
    sql = '''
CREATE TABLE IF NOT EXISTS movie250( 
id INTEGER PRIMARY KEY AUTO_INCREMENT,
info_link TEXT,
pic_link TEXT,
cname VARCHAR(255) ,
ename VARCHAR(255) ,
score NUMERIC ,
rated NUMERIC ,
instroduction TEXT,
info TEXT)
    '''# 创建数据库
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "moviedb")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sqlCheck)
    cursor.execute(sql)
    cursor.close()

if __name__ == "__main__":
    main()
    # init_db()
    print("爬取完毕")