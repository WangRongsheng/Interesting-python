import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment
import matplotlib.pyplot as plt
import os
from sys import platform
from datetime import datetime
from snownlp import SnowNLP



def load_extra_dict(fname, iszip=True):
    sent = sentiment.classifier.classifier
    if not iszip:
        data = marshal.load(open(fname, 'rb'))
    else:
        try:
            data = marshal.loads(gzip.open(fname, 'rb').read())
        except IOError:
            data = marshal.loads(open(fname, 'rb').read())
    for d in data["d"].items():
        if d[0] not in sent.d:
            sent.d[d[0]] = AddOneProb()
        for word, num in d[1]["d"].items():
            sent.d[d[0]].add(word, num)
    sent.total = sum(map(lambda x: sent.d[x].getsum(), sent.d.keys()))

# 拿到爬虫结果，画图
def save_result(qq_msgs="./inputs/msgs.txt", path="./results/my_shuoshuo_sentiment_trend.png"):
    times = []
    sentences = []
    score = []
    with open(qq_msgs, "r", encoding="utf-8") as f:
        lines = f.readlines()
    plt.figure(0, figsize=(7, 5))
    for line in lines:
        if len(line.split("\t")) != 2:
            continue
        time_str, sentence = line.split("\t")
        time = int(time_str)
        s = SnowNLP(sentence)
        # print("{:.3f} {}".format(s.sentiments, sentence))
        times.append(time)
        sentences.append(sentence)
        score.append(s.sentiments)

    plt.plot(score, times)
    ticks = times[::20]
    plt.yticks(ticks, [datetime.fromtimestamp(t).strftime("%Y-%m-%d") for t in ticks])
    plt.xlabel("negative <<<<<<---->>>>>> positive")
    plt.xticks(())
    plt.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    plt.savefig(path)
    plt.close()

# 爬说说
def download_shuoshuo(cookies, path="inputs/msgs.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if platform == "darwin":
        os.system("./shuoshuo -c '%s' -t '%s'" % (cookies, path))
    elif platform == "win32":
        os.system('shuoshuo.exe -c "%s" -t "%s"' % (cookies, path))
    else:
        raise ValueError
