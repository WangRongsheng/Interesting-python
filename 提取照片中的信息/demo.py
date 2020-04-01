'''
图片中怎么存储的信息？可交换图像文件格式（英语：Exchangeable image file format，官方简称Exif），是专门为数码相机的照片设定的，可以记录数码照片的属性信息和拍摄数据。
实用安装：
pip3 install exifread
pip3 install geopy
'''
import exifread
import json
import urllib.request
import sys
from geopy.geocoders import Nominatim
 
# 获取照片的详细信息
def get_img_infor_tup(photo):
    img_file = open(photo, 'rb')
    image_map = exifread.process_file(img_file)
 
    try:
        #图片的经度
        img_longitude_ref = image_map["GPS GPSLongitudeRef"].printable
        img_longitude = image_map["GPS GPSLongitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        img_longitude = float(img_longitude[0])+float(img_longitude[1])/60+float(img_longitude[2])/float(img_longitude[3])/3600
        if img_longitude_ref != "E":
            img_longitude = img_longitude * (-1)
 
        #图片的纬度
        img_latitude_ref = image_map["GPS GPSLatitudeRef"].printable
        img_latitude = image_map["GPS GPSLatitude"].printable[1:-1].replace(" ","").replace("/",",").split(",")
        img_latitude = float(img_latitude[0])+float(img_latitude[1])/60+float(img_latitude[2])/float(img_latitude[3])/3600
        if img_latitude_ref != "N":
            img_latitude = img_latitude*(-1)
 
        #照片拍摄时间
        img_create_date = image_map["EXIF DateTimeOriginal"].printable
 
        img_file.close()
 
        # 返回经纬度元组
        return img_longitude, img_latitude, img_create_date
 
    except Exception as e:
        print('ERROR:图片中不包含Gps信息')
 
# 根据经纬度获取详细的信息
def get_detail_infor(lat, lon):
    reverse_value = str(lat) + ', ' + str(lon)
    geolocator = Nominatim()
    location = geolocator.reverse(reverse_value)
 
    print('照片的经纬度信息：')
    print((location.latitude, location.longitude))
 
    print('照片的地址信息：')
    print(location.address)
    
    print('照片的全部信息：')
    print(location.raw)
 
if __name__ == '__main__':
    infor_tup = get_img_infor_tup('图片名称？？？？？？？')
    get_detail_infor(infor_tup[1], infor_tup[0])
