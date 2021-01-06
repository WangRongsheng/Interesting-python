import re
from xlsxwriter import Workbook
import requests
from lxml import etree

urls = []
infos = []
for i in range(1, 1077):
    urls.append("http://muchong.com/bbs/kaoyan.php?action=adjust&type=1&page={}".format(i))

for k,url in enumerate(urls):
    print("第{}页".format(k + 1))

    con = requests.get(url).content.decode('gbk')

    xp = etree.HTML(con)

    titles = xp.xpath("//tbody[@class='forum_body_manage']/tr")

    for p,i in enumerate(titles):
        print("第{}条".format(p + 1))
        titles_str = etree.tostring(i, encoding='utf-8').decode('utf-8')
        xp_obj = etree.HTML(titles_str)
        title = xp_obj.xpath('//a/text()')[0] if xp_obj.xpath('//a/text()') else "暂无数据"
        school = xp_obj.xpath('//td[2]/text()')[0] if xp_obj.xpath('//td[2]/text()') else "暂无数据"
        cls = xp_obj.xpath('//td[3]/text()')[0] if xp_obj.xpath('//td[3]/text()')[0] != '   ' else "暂无数据"
        stu_num = xp_obj.xpath('//td[4]/text()')[0]
        time = xp_obj.xpath('//td[5]/text()')[0]
        ul = xp_obj.xpath('//a/@href')[0]

        con = requests.get(ul).content

        xpp = etree.HTML(con)

        try:
            ccc = xpp.xpath("//tbody[@id='pid1']//div[@class='t_fsz']//td[@valign='top'][1]")[0].xpath('string(.)')
        except:
            ccc = "暂无数据"
            print(ccc)

        b = re.sub('\r', '', ccc)  # 直接用空字符串替代
        c = re.sub('\n', '', b)  # 直接用空字符串替代
        content = re.sub('\xa0', '', c)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", content) if re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", content) else "暂无数据"

        email = ""
        for e in emails:
            if "@" in e:
                email += e
                email += "  "
            else:
                email = "暂无数据"

        infos.append({"标题": title, "学校": school, "专业_年级":cls, "招生人数":stu_num, "时间":time, "原文链接": ul, "发布内容": content, "邮箱":email})

players = infos
ordered_list = ["标题", "学校", "专业_年级", "招生人数", "发布内容", "邮箱", "时间", "原文链接", ]

wb = Workbook("./%s.xlsx" % "信息")
ws = wb.add_worksheet("New Sheet")

first_row = 0
for header in ordered_list:
    col = ordered_list.index(header)
    ws.write(first_row, col, header)

row = 1
for player in players:
    for _key, _value in player.items():
        col = ordered_list.index(_key)
        ws.write(row, col, _value)
    row += 1
wb.close()
