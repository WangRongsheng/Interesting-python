from snownlp import SnowNLP
from snownlp import sentiment
import marshal
from snownlp.utils.frequency import AddOneProb
import gzip
from snownlp import sentiment
from snownlp import SnowNLP

def train(neg_file, pos_file, to):
    sentiment.train(neg_file, pos_file)
    sentiment.save(to)

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


s = SnowNLP("我喜欢腾讯技术")
print(s.words, " 的正向程度:", s.sentiments)

train("data/test_neg.txt", "data/test_pos.txt","./data/test_sentiment.marshal")
load_extra_dict("./data/test_sentiment.marshal.3")


print(s.words, " 的正向程度:", s.sentiments)
