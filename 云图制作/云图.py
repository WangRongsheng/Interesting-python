from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np

# 生成词云函数
def create_word_cloud(words):
     # 使用结巴分词
     text = " ".join(jieba.cut(words,cut_all=False, HMM=True))
     wc = WordCloud(
           # 字体样式
           font_path=r'C:\Windows\Fonts\simfang.ttf',
           max_words=100,
           width=2000,
           height=1200,
    )
     wordcloud = wc.generate(text)
     # 写词云图片
     wordcloud.to_file("wordcloud.jpg")
     # 显示词云文件
     plt.imshow(wordcloud)
     plt.axis("off")
     plt.show()

s = open("test.txt").read()
create_word_cloud(s)