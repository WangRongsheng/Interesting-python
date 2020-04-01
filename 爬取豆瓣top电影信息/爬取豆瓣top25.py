import requests
import bs4

#抓取网页
def open_url(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"}
    res = requests.get(url,headers=headers)
    
    return res

#得到总页数
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    depth = soup.find('span',class_='next').previous_sibling.previous_sibling.text

    return int(depth)

#解析网页，提取内容
def find_movies(res):
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    names = []
    target = soup.find_all('div',class_='hd')
    for i in target:
        names.append(i.a.span.text)

    ranks = []
    target = soup.find_all('span',class_='rating_num')
    for i in target:
        ranks.append(i.text)

    messages = []
    target = soup.find_all('div',class_='bd')
    for i in target:
        try:
            messages.append(i.p.text.split('\n')[1].strip() + i.p.text.split('\n')[2].strip())
        except:
            continue

    result = []
    length = len(names)
    for i in range(length):
        result.append(names[i] + ',' +ranks[i] + ',' + messages[i] + '\n')

    return result

def main():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(depth):
        url = host + '/?start=' + str(25*i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open("豆瓣TOP250电影.txt",'w',encoding='utf-8') as f:
        for each in result:
            f.write(each)

if __name__=="__main__":
    main()
