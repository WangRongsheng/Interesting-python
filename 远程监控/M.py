from tornado import web, httpserver, ioloop, websocket
import os
import cv2
import numpy as np
from PIL import Image
import base64

# 定义一些基本设置
port = 20210
address = "localhost"
JPEG_HEADER = "data:image/jpeg;base64,"  # 这个是对图片转码用的

# 开启一个摄像头
cap = cv2.VideoCapture(0)


def get_image_dataurl():
    # (1).从摄像头读取数据, 读取成功 ret为True,否则为False,frame里面就是一个三维数组保存图像
    ret, frame = cap.read()
    # (2).先将数组类型编码成 jepg 类型的数据,然后转字节数组,最后将其用base64编码
    r, buf = cv2.imencode(".jpeg", frame)
    dat = Image.fromarray(np.uint8(buf)).tobytes()
    img_date_url = JPEG_HEADER + str(base64.b64encode(dat))[2:-1]
    return img_date_url


class IndexHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class VideoHandler(websocket.WebSocketHandler):

    # 处理接收数据
    def on_message(self, message):
        self.write_message({"img": get_image_dataurl()})


if __name__ == '__main__':
    app = web.Application(handlers=[(r"/", IndexHandler),
                                    (r"/index", IndexHandler),
                                    (r'/video', VideoHandler)],
                          template_path=os.path.join(os.path.dirname(__file__), "ui"))
    http_server = httpserver.HTTPServer(app)
    http_server.listen(port=port, address=address)
    print("URL: http://{}:{}/index".format(address, port))
    ioloop.IOLoop.instance().start()

