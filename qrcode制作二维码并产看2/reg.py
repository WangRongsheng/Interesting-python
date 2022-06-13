import cv2
import pyzbar.pyzbar as pyzbar
import re
import webbrowser

def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取二维码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (225, 225, 225), 2)

        # 提取二维码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (225, 225, 225), 2)

        # 向终端打印条形码数据和条形码类型
        url_res = []
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        url = re.findall(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",barcodeData)
        print(url)
        url_res.append(url)
        if url_res != []:
            webbrowser.open(str(url_res[0][0][0]), new=0, autoraise=True) 
            with open(r"./res.txt", "a+", encoding='utf-8')as f:
                f.seek(0)
                f.truncate()
                f.write(res)
            url_res.clear()
            break
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image


def detect():
    camera = cv2.VideoCapture(0)

    while True:
        # 读取当前帧
        ret, frame = camera.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im = decodeDisplay(gray)

        cv2.waitKey(5)
        cv2.imshow("camera", im)
        # 如果按键q则跳出本次循环
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    detect()
