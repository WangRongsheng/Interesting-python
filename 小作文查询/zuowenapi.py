import json, urllib
from urllib.parse import urlencode
from urllib.request import urlopen

def main():
    # 配置从聚合数据处得到的APPKey
    appkey = "********************************"

    # 1.作文基本信息列表
    request1(appkey, id1=0, id2=0, id3=0, id4=0, m="GET")#request1查询作文基本信息

    # 2.作文内容接口
    request2(appkey, "GET")#request2查询作文具体内容

# 作文基本信息列表
def request1(appkey, id1, id2, id3, id4, m="GET"):
    url = "http://zuowen.api.juhe.cn/zuowen/baseList"
    params = {
        "key": appkey,  # 申请到的APPKEY
        "gradeId": id1,  # 年级id
        "typeId": id2,  # 题材id
        "wordId": id4,  # 字数id
        "level": id3,  # 等级id
        "page": "",  # 页数
    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #请求成功，返回作文基本信息
            print(res["result"])
            return res['result']
        else:
            #请求失败，返回0
            print("%s:%s" % (res["error_code"], res["reason"]))
            return 0 
    else:
        print("request api error")
        return 0 #API错误，返回0


# 作文内容接口
def request2(appkey, idd, m="GET"):

    url = "http://zuowen.api.juhe.cn/zuowen/content"
    params = {
        "key": appkey,  # 已申请的APPKEY
        "id": idd,  # 作文id
    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求,返回查询结果
            print(res["result"])
            return res['result']
        else:
            #请求失败,返回0
            print("%s:%s" % (res["error_code"], res["reason"]))
            return 0
    else:
        print("request api error")
        return 0 #API错误，返回0

if __name__ == '__main__':
    main()
