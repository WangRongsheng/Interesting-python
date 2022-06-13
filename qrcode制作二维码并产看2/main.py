# -*- coding:utf-8 -*-
import os
import qrcode
from PIL import Image
from pyzbar import pyzbar

def make_qr_code_with_icon(content, icon_path, save_path=None):
    if not os.path.exists(icon_path):
        raise FileExistsError(icon_path)

    # First, generate an usual QR Code image
    qr_code_maker = qrcode.QRCode(version=5,
                                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                                  box_size=8,
                                  border=4,
                                  )
    qr_code_maker.add_data(data=content)
    qr_code_maker.make(fit=True)
    qr_code_img = qr_code_maker.make_image(
        fill_color="black", back_color="white").convert('RGBA')

    # Second, load icon image and resize it
    icon_img = Image.open(icon_path)
    code_width, code_height = qr_code_img.size
    icon_img = icon_img.resize(
        (code_width // 4, code_height // 4), Image.ANTIALIAS)

    # Last, add the icon to original QR Code
    qr_code_img.paste(icon_img, (code_width * 3 // 8, code_width * 3 // 8))

    if save_path:
        qr_code_img.save(save_path)  # 保存二维码图片
        qr_code_img.show()  # 显示二维码图片
    else:
        print("保存错误!")


def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)
    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])

if __name__ == "__main__":
    print("1、请输入编码信息（可以为文字、链接、图片地址）：")
    code_Data = input('>>:').strip()
    print("正在编码：")
    # ==生成带中心图片的二维码
    make_qr_code_with_icon(code_Data, "QRcodeCenter.jpg", "qrcode.png")  # 内容，center图片，生成二维码图片
    print("图片已保存，名称为：qrcode.png")
    results = decode_qr_code("qrcode.png")
    print("2、正在解码：")
    if len(results):
        print("解码结果是：")
        res = results[0].data.decode("utf-8")
        print(res)
        with open(r"./info.txt", "a+", encoding='utf-8')as f:
            f.seek(0)
            f.truncate()
            f.write(res)
    else:
        print("无法识别.")
