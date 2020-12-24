import numpy as np
import cv2


def skinmask(img):
    '''

    :param img:
    :return:
    '''

    # 从BGR转换成HSV，即色调、饱和度、明度
    # HSV(Hue、Saturation、Value)基本颜色分量范围，可以参考 https://image.xugaoxiang.com/imgs/2020/12/a3cceeb4f7c9ea2f.jpg
    hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 颜色范围下边界
    lower = np.array([0, 48, 80], dtype="uint8")
    # 颜色范围上边界
    upper = np.array([20, 255, 255], dtype="uint8")

    # 检查数组元素是否位于另外两个数组的元素之间，指定范围内的图像显示为白色，相反为黑色
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)

    # 均值滤波，核大小2*2
    blurred = cv2.blur(skinRegionHSV, (2, 2))

    # 阈值处理，阈值为0，填充色为255，小于阈值的像素点置0，大于阈值的像素点置填255
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)

    return thresh


def getcnthull(mask_img):
    # 找轮廓
    contours, hierarchy = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv2.contourArea(x))

    # 找凸包
    hull = cv2.convexHull(contours)

    return contours, hull


def getdefects(contours):
    # 找凸包，returnPoints=False
    hull = cv2.convexHull(contours, returnPoints=False)

    # 找凸缺陷，也就是我们手指打开时，2指之间凹的部分
    defects = cv2.convexityDefects(contours, hull)

    return defects


if __name__ == '__main__':

    # 读取摄像头数据
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        _, img = cap.read()
        try:
            mask_img = skinmask(img)
            contours, hull = getcnthull(mask_img)

            # 画轮廓
            cv2.drawContours(img, [contours], -1, (255, 255, 0), 2)
            cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)

            # 轮廓线为convexity hull, 而convexity hull与手掌之间的部分为convexity defects。每个convexity defect区域有四个特征量：起始点（startPoint），结束点(endPoint)，距离convexity hull最远点(farPoint)，最远点到convexity hull的距离(depth)。
            defects = getdefects(contours)
            if defects is not None:
                cnt = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i][0]
                    start = tuple(contours[s][0])
                    end = tuple(contours[e][0])
                    far = tuple(contours[f][0])

                    # 得到三角形3条边的长度
                    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

                    # 使用余弦定理计算角度
                    angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

                    # 如果角度小于90度，则认为是手指
                    if angle <= np.pi / 2:
                        cnt += 1
                        cv2.circle(img, far, 4, [0, 0, 255], -1)
                if cnt > 0:
                    cnt = cnt + 1

                # 显示手指个数
                cv2.putText(img, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("img", img)
        except:
            pass

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
