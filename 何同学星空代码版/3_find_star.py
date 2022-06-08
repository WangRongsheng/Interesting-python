from pickle import TRUE
from turtle import distance
import cv2
from cv2 import waitKey
import numpy as np
import os
from  tqdm import tqdm

def txt2array(txt_path, delimiter):
    #---
    # 功能：读取只包含数字的txt文件，并转化为array形式
    # txt_path：txt的路径；delimiter：数据之间的分隔符
    #---
    data_list = []
    with open(txt_path) as f:
        data = f.readlines()
    for line in data:
        line = line.strip("\n")  # 去除末尾的换行符
        data_split = line.split(delimiter)
        temp = list(map(float, data_split))
        data_list.append(temp)

    data_array = np.array(data_list)
    return data_array

def erose_img(img,img_mask,yz,):
    original_img=img
    # 图形太大，执行缩小操作
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(img_mask,kernel)
    sp=original_img.shape
    # cv2.imshow("src",original_img)
    gray1 = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(erosion, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("erosion",erosion)
    chazhi=[]
    for i in range(sp[0]):
        for m in range(sp[1]):
            # chazhi[i][m]=0
                num1=int(gray1[i][m])
                num2=int(gray2[i][m])
                if((num1-num2)>yz):
                    # if(chazhi):
                    #     x1=chazhi[-1][0]
                    #     y1=chazhi[-1][1]                   
                    #     r=pow(pow(x1-i,2)+pow(y1-m,2),0.5)
                    #     if(r>200):
                    #         chazhi.append([i,m,num1])
                    # else:
                         chazhi.append([i,m,num1])
    new_list = sorted(chazhi, key = lambda x:x[2],reverse=True)  
    return new_list

def canny(img):
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianBlur = cv2.GaussianBlur(grayImage, (3, 3), 0)
    gaussian = cv2.GaussianBlur(grayImage, (5, 5), 0)
    Canny = cv2.Canny(gaussian, 50, 150)
    sp=grayImage.shape
    chazhi=[]
    for i in range(sp[0]):
        for m in range(sp[1]):
            if(Canny[i][m]==255):
                # if(chazhi):
                #     x1=chazhi[-1][0]
                #     y1=chazhi[-1][1]                   
                #     r=pow(pow(x1-i,2)+pow(y1-m,2),0.5)
                #     if(r>200):
                #         chazhi.append([i,m,grayImage[i][m]])
                # else:
                    chazhi.append([i,m,grayImage[i][m]])
    new_list = sorted(chazhi, key = lambda x:x[2],reverse=True)   
    return new_list

def chazhi(gray1,gray2,yz):
    sp=gray1.shape
    chazhi=[]

    for i in range(sp[0]):
        for m in range(sp[1]):
            # chazhi[i][m]=0
            num1=int(gray1[i][m])
            num2=int(gray2[i][m])
            if((num1-num2)>yz):
                # if(chazhi):
                #     x1=chazhi[-1][0]
                #     y1=chazhi[-1][1]                   
                #     r=pow(pow(x1-i,2)+pow(y1-m,2),0.5)
                #     if(r>200):
                #         chazhi.append([i,m,num1])
                # else:
                    chazhi.append([i,m,num1])
    
    new_list = sorted(chazhi, key = lambda x:x[2],reverse=True)
    return new_list

def yishiying(gray1,keral_size,offset):
    img_ret12 = cv2.adaptiveThreshold(gray1,  255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,keral_size,offset) 
    sp=gray1.shape
    chazhi=[]
    for i in range(sp[0]):
        for m in range(sp[1]):
            if(img_ret12[i][m]==255):
                # if(chazhi):
                #     x1=chazhi[-1][0]
                #     y1=chazhi[-1][1]                   
                #     r=pow(pow(x1-i,2)+pow(y1-m,2),0.5)
                #     if(r>200):
                #         chazhi.append([i,m,gray1[i][m]])
                # else:
                    chazhi.append([i,m,gray1[i][m]])
    new_list = sorted(chazhi, key = lambda x:x[2],reverse=True)   
    return new_list

# file_FOLDER=星轨原图所在地
# pat=图案名称
# yz=canny的阈值，阈值越大，筛选的星星越少
# size_change=图案在照片上的大小，数值越大，大小越小
# method可选四种星星筛选方式，填入对应字符串'jubuyuzhi','chazhi','canny','erose',
# IsJianbian=图案是否以渐变方式出现，填入bool值
def MyStar(file_FOLDER,pat,yz,midu,size_change,method,IsJianbian):
    dirs = os.listdir( file_FOLDER )
    path_file_FOLDER='path_txt/'+pat+'/'
    lujing_dirs=os.listdir(path_file_FOLDER)
    epoch=len(lujing_dirs)
    size=len(dirs)
    num_pic=0
    mask_img=cv2.imread(file_FOLDER+'/'+dirs[0]) 
    mask_img=cv2.resize(mask_img,(1920,1080))
    for k in tqdm(range(0,size)):
        filepath1=file_FOLDER+'/'+dirs[k]
        filepath2=file_FOLDER+'/'+dirs[(k+int(size/2))%size]
        img1 = cv2.imread(filepath1)   #读取图片
        img2 = cv2.imread(filepath2)   #读取图片

        # img1=cv2.resize(img1,(1920,1080))
        # img2=cv2.resize(img2,(1920,1080))
        
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  #变为灰度图 
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  #变为灰度图 
        
        sp=gray1.shape
        if(method=='chazhi'):
            star_pos_img=chazhi(gray1,gray2,yz)
        if(method=='canny'):
            star_pos_img=canny(img1)
        if(method=='erose'):
            star_pos_img=erose_img(img1,mask_img,100)
        if(method=='jubuyuzhi'):
            star_pos_img=yishiying(gray1,9,-25)


        # if(num_pic==0):
        #     cv2.namedWindow(method, 0)    
        #     cv2.resizeWindow(method, sp[0], sp[1])   # 自己设定窗口图片的大小
        #     cv2.imshow(method, star_pos_img)
        #     cv2.waitKey(0)


        filename='output/'+file_FOLDER[-1]+'_'+pat+'_'+method+'/'
        if not os.path.exists(filename):
            #如果文件目录不存在则创建目录
            os.makedirs(filename) 
        with open(filename+'pos_info.txt','ab') as f:
            np.savetxt(f,star_pos_img[0:20], fmt='%d', delimiter=',',header=dirs[k])


        filename=filename+dirs[k]
        if(os.path.exists(filename)):
            continue
        w,h = img1.shape[:-1]  #获取长宽
        print(w,h)
        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  #变为灰度图 
        cur_path_file=path_file_FOLDER+lujing_dirs[num_pic%epoch]

        cur_path_file=path_file_FOLDER+lujing_dirs[num_pic%epoch]
        array = txt2array(cur_path_file,',')
        num=len(array)
        for point in range(40):#这里的40也可更改，数值越大，图上的星星越多
            if(not(IsJianbian)):
                i=star_pos_img[point][0]
                m=star_pos_img[point][1]
                for x in range(0,num,midu):
                    offset_y=int(array[x][0]*size_change)
                    offset_x=int(array[x][1]*size_change)
                    if(i+offset_y<w and i+offset_y>=0 and m+offset_x<h and m+offset_x>=0):
                        img1[i+offset_y][m+offset_x]=img1[i][m] 
            else:
                i=star_pos_img[point][0]
                m=star_pos_img[point][1]
                if(num_pic<24):
                    for x in range(0,int(num*num_pic/24),midu):
                        offset_y=int(array[x][0]*size_change)
                        offset_x=int(array[x][1]*size_change)
                        if(i+offset_y<w and i+offset_y>=0 and m+offset_x<h and m+offset_x>=0):
                                img1[i+offset_y][m+offset_x]=img1[i][m]
                else:                
                    for x in range(0,num,midu):
                        offset_y=int(array[x][0]*size_change)
                        offset_x=int(array[x][1]*size_change)
                        if(i+offset_y<w and i+offset_y>=0 and m+offset_x<h and m+offset_x>=0):
                                img1[i+offset_y][m+offset_x]=img1[i][m]                                  
        if(num_pic==0):
            cv2.namedWindow('preview', 0)    
            cv2.resizeWindow('preview', w, h)   # 自己设定窗口图片的大小
            cv2.imshow("preview", img1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        cv2.imwrite(filename,img1,[cv2.IMWRITE_JPEG_QUALITY, 100])
        num_pic=num_pic+1

file_FOLDER = 'yuantu/4'  #！！！文件夹的地址（手动修改）
pat='people' 
yz=0
midu=2 # 密度为图案沿线的密度，数值越小，图案路径上的点越多
size_change=1
method='chazhi'
IsJianbian=True
MyStar(file_FOLDER,pat,yz,midu,size_change,method,IsJianbian)      
