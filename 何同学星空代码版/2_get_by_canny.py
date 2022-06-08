import cv2
from matplotlib.pyplot import flag
import numpy as np  
import os


def MyCanny_Edge(pat):
    file_FOLDER='pattern/'+pat+'/'
    img_name = os.listdir( file_FOLDER )
    for z in img_name:
        original_img = cv2.imread(file_FOLDER+z, 0)
        sp=original_img.shape
        # canny(): 边缘检测
        img1 = cv2.GaussianBlur(original_img,(3,3),0)
        canny = cv2.Canny(img1, 50, 240)
        if(z==img_name[0]):
            cv2.namedWindow('preview', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('preview', canny)
            cv2.waitKey(0)
        sp=canny.shape
        a=[]
        start_x=sp[0]/2
        start_y=sp[1]/2
        for i in range(sp[0]):
            for k in range(sp[1]):
                if(canny[i][k]!=0):
                    a.append([i-start_x,k-start_y])
        outPutDirName='path_txt/'+pat+'/'
        if not os.path.exists(outPutDirName):
                #如果文件目录不存在则创建目录
            os.makedirs(outPutDirName) 
        file_path=z+'_lujing.txt'
        np.savetxt(outPutDirName+file_path,a, fmt='%d', delimiter=',')

pat='people' #！！！需要手动修改的花纹选项
MyCanny_Edge(pat)
