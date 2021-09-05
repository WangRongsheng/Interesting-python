import jieba
import requests
import string
import time
import random
import json
inf = int(1e9)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'referer': 'https://www.bilibili.com/'
}


def get_score(c):
    punc = string.punctuation
    if c in punc:
        return 2
    c = c.encode('utf-8')
    if c.isalnum():
        return 3
    return 5


def get_sim(s, target):
    pos = s.find(target)
    if pos == -1:
        return inf
    sum = 0
    for c in s[0:pos]:
        sum += get_score(c)
    for c in s[pos+len(target):]:
        sum += get_score(c)
    sum /= len(target)
    return sum


def find_bili_user(target):
    time.sleep(random.uniform(1, 3))
    try:
        b = requests.get(
            url='https://api.bilibili.com/x/web-interface/search/type?keyword=%s&search_type=bili_user' % target, headers=headers).json()
        users = b['data']['result']
    except:
        return {'score': inf, 'users': []}
    page_num = min(5, b['data']['numPages'])
    for i in range(2, page_num):
        time.sleep(random.uniform(1, 3))
        try:
            users.extend(requests.get(url='https://api.bilibili.com/x/web-interface/search/type?keyword=%s&search_type=bili_user&page=%d' %
                                      (target, i), headers=headers).json()['data']['result'])
        except:
            pass
    best = inf
    res = {}
    for p in users:
        name = p['uname']
        k = get_sim(name, target)
        if k < best:
            best = k
            res = {'level': p['level'], 'uname': p['uname'],
                   'upic': p['upic'], 'usign': p['usign'], 'uid': p['mid'], 'fans': p['fans'], 'videos': p['videos']}
    if best == inf:
        return {'score': inf, 'users': []}
    #print(target, best, res['uname'])
    return {'score': best, 'users': [res]}


mem = {}


def calc(a):
    s = ''.join(a)
    if s in mem:
        return mem[s]
    res = find_bili_user(s)
    if res['score'] == 0:
        mem[s] = res
        return res
    for i in range(1, len(a)):
        res1 = calc(a[0:i])
        res2 = calc(a[i:])
        score = res1['score'] + res2['score'] + 6 / len(s)
        if res['score'] > score:
            res = {'score': score, 'users': res1['users'] + res2['users']}
    mem[s] = res
    return res


output = []


def calcline(s):
    res = calc(list(jieba.cut(s)))
    for p in res['users']:
        print(p['uname'], end=' ')
    print('')
    return res


jieba.lcut('开始')
f = open('music.lrc').readlines()
for s in f:
    s = s.replace('[', ']').split(']')
    s[2] = s[2].replace('\n', '')
    if len(s[2]) == 0:
        continue
    print(s[2])
    res = calcline(s[2])
    res['lyric'] = s[2]
    res['time'] = s[1]
    output.append(res)
    open('res.json', 'w', encoding='utf-8').write(json.dumps(output, indent=4,
                                                             separators=(',', ': '), ensure_ascii=False))
