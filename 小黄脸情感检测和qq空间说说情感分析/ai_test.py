from snownlp import SnowNLP
from snownlp import sentiment
from utils import load_extra_dict

def train(neg_file, pos_file, to):
    sentiment.train(neg_file, pos_file)
    sentiment.save(to)


# train("data/test_neg.txt", "data/test_pos.txt", "data/test_sentiment.marshal")

s = SnowNLP("我喜欢腾讯技术")
print(s.words, "正向程度", s.sentiments)
load_extra_dict("data/test_sentiment.marshal.3")
print(s.words, "正向程度", s.sentiments)

