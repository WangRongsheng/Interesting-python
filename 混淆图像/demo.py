from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#获取图片三维像素通道矩阵
img=np.array(Image.open('7.jpg'))
row_len=img.shape[0]#第一维度
#打乱维度索引
row_index=np.random.permutation(row_len)
img_chaos=img[row_index,:,:]#生成混淆图
#利用排序解混图
img_sort=img[np.sort(row_index),:,:]
#画出混淆图和解混图
plt.figure("混淆图和解混图")
plt.subplot(211)
plt.imshow(img_chaos)
plt.subplot(212)
plt.imshow(img_sort)
plt.show()
