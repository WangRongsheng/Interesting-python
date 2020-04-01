import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation


class KMeans(object):
    def __init__(self, data):
        '''
        data: 要分类的数据，二维数组，每一行是一个样本，列数为样本特征数
        '''
        self.data = data
        self.calc_classes = np.frompyfunc(          # 自定义ufunc，将所有样本分类
            self.calc_distance, data.shape[1], 1)

        self.fig, self.ax = plt.subplots()


    def calc_distance(self, *features):
        '''
        计算单个样本与每个中心的距离，然后将其归于最近的一类
        features: 样本的特征值
        返回样本新的类别
        '''
        x = np.array(features)      # 将样本的特征转换为一个向量
        return np.argmin(np.square(self.center - x).sum(axis=1))


    def clustering(self, k):
        '''
        k: 要聚类的数量
        '''
        self.k = k
        self.sizes = np.linspace(40, 100, num=k)
        choices = np.random.randint(0, self.data.shape[0], size=k) 
        self.center = np.copy(self.data[choices])   # 从data中随机选取k行作为随机中心
        
        anim = FuncAnimation(self.fig,  # 设置动画
                func=self.update,       # 回调函数，FuncAnimation会在每一帧都调用该函数
                frames=np.arange(8),    # 帧数
                init_func=self.setup,   # 动画初始化
                interval=1000)          # 每帧间隔
        anim.save('clustering.gif', dpi=80, writer='pillow')


    def setup(self, colors=['r', 'g', 'b', 'k']):
        '''
        动画初始化函数
        '''
        cs = self.get_classified_sample()
        
        tmp = []
        for i in np.arange(self.k):     # 绘制已分类的样本
            tmp.append(self.ax.scatter(cs[i][:,0], cs[i][:,1], c=colors[i], animated=True))

        for i in np.arange(self.k):     # 绘制中心
            tmp.append(self.ax.scatter(self.center[i,0], self.center[i,1], c=colors[i], s=150, marker='x', animated=True))

        self.sc = tuple(tmp)            # 必须转换为元组

        for i in np.arange(self.k):     # 更新每个簇的中心
            self.center[i,:] = cs[i].mean(axis=0)

        return self.sc      # 返回必须是元组


    def get_classified_sample(self):
        '''
        将所有样本分为k类
        返回一个列表，列表中的每个元素是被归于同一类的样本
        '''
        cols = list(self.data.T)
        self.classes = self.calc_classes(*cols)     # 计算所有样本的类别
        return [self.data[self.classes==i] for i in np.arange(self.k)]


    def update(self, j):
        print(j)

        cs = self.get_classified_sample()

        for i in np.arange(self.k):
            self.sc[i].set_offsets(cs[i])                       # 更新每个簇的点的坐标
            self.sc[i]._sizes[0] = self.sizes[(i+j) % self.k]   # 动态调增点的大小，增加视觉对比
            self.sc[i+self.k].set_offsets(self.center[i])       # 更新每个簇中心的坐标


        for i in np.arange(self.k):         # 更新每个簇的中心
            self.center[i,:] = cs[i].mean(axis=0)

        return self.sc      # 返回必须是元组

if __name__ == "__main__":

    data = np.loadtxt('./test.txt')
    km = KMeans(data)
    km.clustering(4)
